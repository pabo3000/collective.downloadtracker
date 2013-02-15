from AccessControl import ClassSecurityInfo
from Products.CMFCore.permissions import View
from collective.downloadtracker import add_download_record

security = ClassSecurityInfo()


security.declareProtected(View, 'download')
def download(self, instance, REQUEST=None, RESPONSE=None):
    """ download the file (use default index_html) """
    add_download_record(instance)
    return self.index_html(instance,
                           REQUEST,
                           RESPONSE,
                           disposition='attachment')
