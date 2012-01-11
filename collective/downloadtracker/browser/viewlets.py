# -*- coding: utf-8 -*-
"""Viewlets."""
from Acquisition import aq_inner
from AccessControl.SecurityManagement import getSecurityManager

from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone.app.layout.viewlets import ViewletBase
from plone.memoize.view import memoize

class DownloadRecordsViewlet(ViewletBase):
    """Browser view for displaying download records."""
    render = ViewPageTemplateFile("download_records.pt")

    def __init__(self, context, request, view, manager):
        self.context = context
        super(DownloadRecordsViewlet, self).__init__(context, request, view, manager)

    @memoize
    def has_download_records(self):
        """Checks if this File has a download_records field."""
        return hasattr(self.context, 'download_records')

    @memoize
    def download_records(self):
        return self.context.getField('download_records').get(self.context)

    def can_manage(self):
        return getSecurityManager().checkPermission('Manage portal', aq_inner(self.context))