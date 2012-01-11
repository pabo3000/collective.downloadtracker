import json

from Products.Five.browser import BrowserView

class DeleteDownloadRecord(BrowserView):

    # by default call will call self.index() method which is mapped
    # to ViewPageTemplateFile specified in ZCML
    def __call__(self):
        # Make sure any theming layer won't think this is HTML
        # http://stackoverflow.com/questions/477816/the-right-json-content-type
        self.request.response.setHeader("Content-type", "application/json")
        name = self.request.get("name", None)
        date = self.request.get("date", None)
        record = (name, date)
        field = self.context.getField('download_records')
        download_records = field.get(self.context)
        # is record in download_records
        try:
            i = download_records.index(record)
        except ValueError:
            return 'false'
        del download_records[i]
        field.set(self.context, download_records)
        return 'true'