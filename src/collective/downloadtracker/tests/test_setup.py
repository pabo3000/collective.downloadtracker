# -*- coding: utf-8 -*-
"""Setup/installation tests for this package."""

from collective.downloadtracker.testing import IntegrationTestCase
from plone import api


class TestInstall(IntegrationTestCase):
    """Test installation of collective.downloadtracker into Plone."""

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if collective.downloadtracker is installed with portal_quickinstaller."""
        self.assertTrue(self.installer.isProductInstalled('collective.downloadtracker'))

    def test_uninstall(self):
        """Test if collective.downloadtracker is cleanly uninstalled."""
        self.installer.uninstallProducts(['collective.downloadtracker'])
        self.assertFalse(self.installer.isProductInstalled('collective.downloadtracker'))

    # browserlayer.xml
    def test_browserlayer(self):
        """Test that ICollectiveDownloadtrackerLayer is registered."""
        from collective.downloadtracker.interfaces import IDownloadtrackerInstalled
        from plone.browserlayer import utils
        self.failUnless(IDownloadtrackerInstalled in utils.registered_layers())
