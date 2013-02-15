# -*- coding: utf-8 -*-
"""Module where all interfaces, events and exceptions live."""

import zope.interface


class IDownloadtrackerInstalled(zope.interface.Interface):
    """A layer specific for this add-on product.

    This interface is referred in browserlayers.xml.

    All views and viewlets register against this layer will appear on your
    Plone site only when the add-on installer has been run.
    """
