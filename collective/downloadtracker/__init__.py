# -*- coding: utf-8 -*-
"""Initializer."""
import json
import AccessControl
from DateTime import DateTime
from zope.app.component.hooks import getSite
from Products.CMFCore.utils import getToolByName


# Allow access to increase_download_count() from Script (Python)
AccessControl.ModuleSecurityInfo('collective.downloadtracker').declarePublic('add_download_record')

def getActiveUserName():
    """ Return the username of the current user, or None.
    """
    portal = getSite()
    mt = getToolByName(portal, 'portal_membership')
    if mt.isAnonymousUser(): # the user has not logged in
        return None
    else:
        member = mt.getAuthenticatedMember()
        username = member.getUserName()
        return username

def add_download_record(file):
    """Adds new download record on a File."""
    if hasattr(file, 'download_records'):
        download_records = list(file.download_records)
        # logged-in member
        username = getActiveUserName()
        download_records.append(json.dumps((username, DateTime().strftime("%d.%m.%Y %H:%M"))))
        file.download_records = download_records

def initialize(context):
    """Initializer called when used as a Zope 2 product."""


