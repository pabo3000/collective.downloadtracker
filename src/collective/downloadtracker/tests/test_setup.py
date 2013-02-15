# -*- coding: utf-8 -*-
"""Setup/installation tests for this package."""

import DateTime
import os.path
from collective.downloadtracker.testing import IntegrationTestCase, \
    FunctionalTestCase
from collective.downloadtracker import getActiveUserName, add_download_record
from plone import api

from plone.app.testing import SITE_OWNER_NAME
from plone.app.testing import SITE_OWNER_PASSWORD
from plone.testing.z2 import Browser

from collective.downloadtracker.testing import FUNCTIONAL_TESTING


class TestInstall(IntegrationTestCase):
    """Test installation of collective.downloadtracker into Plone."""

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """ Test if collective.downloadtracker is installed
            with portal_quickinstaller. """
        self.assertTrue(
            self.installer.isProductInstalled('collective.downloadtracker'))

    def test_uninstall(self):
        """Test if collective.downloadtracker is cleanly uninstalled."""
        self.installer.uninstallProducts(['collective.downloadtracker'])
        self.assertFalse(
            self.installer.isProductInstalled('collective.downloadtracker'))

    # browserlayer.xml
    def test_browserlayer(self):
        """Test that ICollectiveDownloadtrackerLayer is registered."""
        from collective.downloadtracker.interfaces \
            import IDownloadtrackerInstalled
        from plone.browserlayer import utils
        self.failUnless(IDownloadtrackerInstalled in utils.registered_layers())

    def test_field_download_records(self):
        file = self.portal.file1
        self.assertTrue(file.getField('download_records'))
        file.getField('download_records').set(file,
                                              '["pab", "15.02.2013 14:01"]')
        self.assertEqual(file.getField('download_records').get(file),
                         [(u'pab', u'15.02.2013 14:01')])

    def test_getActiveUserName(self):
        self.assertEqual(getActiveUserName(), u'test-user')

    def test_add_download_record(self):
        file = self.portal.file1
        add_download_record(file)
        user, ts = file.getField('download_records').get(file)[0]
        self.assertEqual(user, u'test-user')
        self.assertTrue(isinstance(DateTime.DateTime(ts), DateTime.DateTime))


class FileFunctionalTest(FunctionalTestCase):

    layer = FUNCTIONAL_TESTING

    def setUp(self):
        app = self.layer['app']
        self.portal = self.layer['portal']
        self.request = self.layer['request']
        self.portal_url = self.portal.absolute_url()
        self.browser = Browser(app)
        self.browser.handleErrors = False
        self.browser.addHeader(
            'Authorization',
            'Basic %s:%s' % (SITE_OWNER_NAME, SITE_OWNER_PASSWORD,)
        )

    def test_add_file(self):
        self.browser.open(self.portal_url)
        self.browser.getLink('File').click()
        self.assertTrue('Title' in self.browser.contents)
        self.assertTrue('Description' in self.browser.contents)
        self.browser.getControl(name='title')\
            .value = "My file"
        self.browser.getControl(name='description')\
            .value = "This is my file."
        file_path = os.path.join(os.path.dirname(__file__), "image.jpg")
        file_ctl = self.browser.getControl(name='file_file')
        file_ctl.add_file(open(file_path), 'image/png', 'image.jpg')
        self.browser.getControl('Save').click()
        self.assertTrue(self.browser.url.endswith('my-file/view'))
        self.assertTrue('My file' in self.browser.contents)
        self.assertTrue('This is my file' in self.browser.contents)

        self.browser.getLink('image.jpg').click()
        self.browser.open(self.portal_url)
        self.browser.getLink('My file').click()
        self.assertTrue('admin' in self.browser.contents)
        self.browser.getLink('x').click()
        # x triggers a javascript, so it does not work in testbrowser
