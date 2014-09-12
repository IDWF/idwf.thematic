from collective.grok import gs
from idwf.thematic import MessageFactory as _

@gs.importstep(
    name=u'idwf.thematic', 
    title=_('idwf.thematic import handler'),
    description=_(''))
def setupVarious(context):
    if context.readDataFile('idwf.thematic.marker.txt') is None:
        return
    portal = context.getSite()

    # do anything here
