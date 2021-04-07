# -*- coding: utf-8 -*-
from plone.indexer import indexer
from plone.app.contenttypes.behaviors.leadimage import ILeadImage


@indexer(ILeadImage)
def leadImageFile(context):
    """Create a catalogue indexer, registered as an adapter, which can
    populate the ``context.filename`` value and index it.
    """
    return context.image.filename
