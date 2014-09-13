from five import grok
from zope.schema.interfaces import IContextSourceBinder
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm
from zope.schema.interfaces import IVocabularyFactory
from zope.component import getUtility
from z3c.formwidget.query.interfaces import IQuerySource

class thematic(grok.GlobalUtility):
    grok.name('idwf.thematic.thematic')
    grok.implements(IVocabularyFactory)

    _terms = [
        {
            'value': 'c189',
            'title': 'C189 Ratification',
        },
        {
            'value': 'child domestic workers',
            'title': 'Child Domestic Workers',
        },
        {
            'value': 'collective bargaining',
            'title': 'Collective Bargaining',
        },
        {
            'value': 'communication',
            'title': 'Communication',
        },
        {
            'value': 'hoursofwork',
            'title': 'Days Off & Hours of work',
        },
        {
            'value': 'dignity',
            'title': 'Dignity of Domestic Workers',
        },
        {
            'value': 'bills',
            'title': 'Domestic Workers Bills',
        },
        {
            'value': 'working conditions',
            'title': 'Employment & Working Conditions',
        },
        {
            'value': 'forced labour',
            'title': 'Forced Labour',
        },
        {
            'value': 'history',
            'title': 'History',
        },
        {   'value': 'migrant',
            'title': 'Migrant Domestic Workers',
            },
        {   'value': 'occupational safety',
            'title': 'Occupational Safety & Health',
            },
        {   'value': 'research',
            'title': 'Participatory Research',
            },
        {   'value': 'private agencies',
            'title': 'Private Employment Agencies',
            },
        {   'value': 'organize',
            'title': 'Rights to Organize',
            },
        {   'value': 'harassment',
            'title': 'Sexual Harassment',
            },
        {   'value': 'worker rights',
            'title': "Workers' Rights",
            },
        ]

    def __call__(self, context):
        terms = []
        for i in self._terms:
            terms.append(SimpleTerm(**i))
        return SimpleVocabulary(terms)
