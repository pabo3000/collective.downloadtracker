from AccessControl import ClassSecurityInfo
from Products.CMFCore.permissions import View
from collective.downloadtracker import add_download_record

security = ClassSecurityInfo()


security.declareProtected(View, 'index_html')
def index_html(self, instance, REQUEST=None, RESPONSE=None, **kwargs):
    """ make it directly viewable when entering the objects URL """
    blob = self.get(instance, raw=True)    # TODO: why 'raw'?
    charset = instance.getCharset()
    add_download_record(instance)
    return blob.index_html(
        REQUEST=REQUEST, RESPONSE=RESPONSE,
        charset=charset, **kwargs
        )