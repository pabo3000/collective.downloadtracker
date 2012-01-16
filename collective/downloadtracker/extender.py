# -*- coding: utf-8 -*-
"""Extend default Plone content types."""
import json

from AccessControl import ClassSecurityInfo

from zope.component import adapts
from zope.interface import implements

from Products.Archetypes.public import LinesWidget, LinesField
from Products.Archetypes.Field import ObjectField, encode
from Products.ATContentTypes.interface import IATFile

from archetypes.schemaextender.interfaces import ISchemaExtender, IBrowserLayerAwareExtender
from archetypes.schemaextender.field import ExtensionField

from interfaces import IDownloadtrackerInstalled

def sortedDictValues(adict):
    items = adict.items()
    items.sort()
    return [(value, key) for key, value in items]

class _MyLinesField(ExtensionField, LinesField):
    """A simple lines field."""

    security  = ClassSecurityInfo()

    security.declarePrivate('set')
    def set(self, instance, value, **kwargs):
        """
        The list of tuples is internally stored as a list of strings.
        The format of such a string is: "name: date".
        """
        if isinstance(value, list):
            value = [json.dumps((k, v)) for k, v in value]
        super(_MyLinesField, self).set(instance, value, **kwargs)

    security.declarePrivate('get')
    def get(self, instance, **kwargs):
        """
        Getter which returns value as sorted list of tuples.
        """
        value = ObjectField.get(self, instance, **kwargs) or ()
        data = [encode(v, instance, **kwargs) for v in value]
        adict = {}
        for record in data:
            try:
                value, key = json.loads(record)
            except ValueError:
                key = record
                value = None
            adict[key] = value
        return sortedDictValues(adict)

class FileExtender(object):
    """Extends default File content type."""
    adapts(IATFile)
    implements(ISchemaExtender, IBrowserLayerAwareExtender)
    layer = IDownloadtrackerInstalled

    fields = [
        _MyLinesField(
            "download_records",
            widget = LinesWidget(
                label=u"Download Records",
                description=u"When was this file downloaded from whom", 
                modes=('view', )
                ),
            default=[],
            ),
            ]

    def __init__(self, context):
        self.context = context

    def getFields(self):
        return self.fields
