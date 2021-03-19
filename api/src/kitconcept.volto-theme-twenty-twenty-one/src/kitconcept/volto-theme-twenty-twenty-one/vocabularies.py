from plone import api
from zope.interface import provider
from zope.schema.interfaces import IVocabularyFactory
from zope.schema.vocabulary import SimpleTerm
from zope.schema.vocabulary import SimpleVocabulary


@provider(IVocabularyFactory)
def simple_vocabulary(context):
    return SimpleVocabulary(
        [
            SimpleTerm(value=u"barcelona-catalonia", title=u"Barcelona, Catalonia"),
            SimpleTerm(value=u"bonn-germany", title=u"Bonn, Germany"),
            SimpleTerm(value=u"other", title=u"Other Location"),
        ]
    )


@provider(IVocabularyFactory)
def dynamic_vocab(context):
    pc = api.portal.get_tool("portal_catalog")
    brains = pc.searchResults(portal_type="Events")
    terms = []
    for brain in brains:
        terms.append(SimpleTerm(value=brain.getPath(), title=brain.Title))

    return SimpleVocabulary(terms)
