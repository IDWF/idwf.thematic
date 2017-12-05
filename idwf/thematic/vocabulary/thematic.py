from five import grok
from zope.schema.interfaces import IContextSourceBinder
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm
from zope.schema.interfaces import IVocabularyFactory
from zope.component import getUtility
from z3c.formwidget.query.interfaces import IQuerySource

from idwf.thematic import MessageFactory as _

class thematic(grok.GlobalUtility):
    grok.name('idwf.thematic.thematic')
    grok.implements(IVocabularyFactory)

    _terms = [
        {
            'value': 'c189',
            'title': _(u'C189 Ratification'),
        },
        {
            'value': 'child domestic workers',
            'title': _(u'Child Domestic Workers'),
        },
        {
            'value': 'collective bargaining',
            'title': _(u'Collective Bargaining'),
        },
        {
            'value': 'communication',
            'title': _(u'Communication'),
        },
        {
            'value': 'hoursofwork',
            'title': _(u'Days Off & Hours of work'),
        },
        {
            'value': 'dignity',
            'title': _(u'Dignity of Domestic Workers'),
        },
        {
            'value': 'bills',
            'title': _(u'Domestic Workers Bills'),
        },
        {
            'value': 'working conditions',
            'title': _(u'Employment & Working Conditions'),
        },
        {
            'value': 'forced labour',
            'title': _(u'Forced Labour'),
        },
        {
            'value': 'history',
            'title': _(u'History'),
        },
        {   'value': 'migrant',
            'title': _(u'Migrant Domestic Workers'),
            },
        {   'value': 'occupational safety',
            'title': _(u'Occupational Safety & Health'),
            },
        {   'value': 'research',
            'title': _(u'Participatory Research'),
            },
        {   'value': 'private agencies',
            'title': _(u'Private Employment Agencies'),
            },
        {   'value': 'organize',
            'title': _(u'Rights to Organize'),
            },
        {   'value': 'harassment',
            'title': _(u'Sexual Harassment'),
            },
        {   'value': 'worker rights',
            'title': _(u"Workers' Rights"),
            },
        ]

    def __call__(self, context):
        terms = []
        for i in self._terms:
            terms.append(SimpleTerm(**i))
        return SimpleVocabulary(terms)
