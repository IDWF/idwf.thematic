from five import grok
from zope.schema.interfaces import IContextSourceBinder
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm
from zope.schema.interfaces import IVocabularyFactory
from zope.component import getUtility
from z3c.formwidget.query.interfaces import IQuerySource

class thematic(grok.GlobalUtility):
    grok.name('idwf.thematic.thematic')
    grok.implements(IVocabularyFactory)

    _terms = [{
        'value': 'termvalue',
        'title': 'Term Title',
        'token': 'termtoken',
    }]

    def __call__(self, context):
        terms = [(u'child domestic workers'),_(u'Child Domestic Works')]
        for i in self._terms:
            terms.append(SimpleTerm(**i))
        return SimpleVocabulary(terms)
