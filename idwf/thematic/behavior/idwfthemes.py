from zope.interface import alsoProvides, implements
from zope.component import adapts
from zope import schema
from plone.directives import form
from plone.dexterity.interfaces import IDexterityContent
from plone.autoform.interfaces import IFormFieldProvider

from plone.namedfile import field as namedfile
from z3c.relationfield.schema import RelationChoice, RelationList
from plone.formwidget.contenttree import ObjPathSourceBinder

from idwf.thematic import MessageFactory as _

class IIDWFThemes(form.Schema):
    """
       Marker/Form interface for IDWF Themes
    """

    # -*- Your Zope schema definitions here ... -*-

    idwf_themes = schema.List(
            title = _(u'Theme(s)'),
            value_type = schema.Choice(
                vocabulary = "idwf.thematic.thematic",
                ),
            required=False,
            )

alsoProvides(IIDWFThemes,IFormFieldProvider)
