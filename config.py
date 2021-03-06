###
# Copyright (c) 2014, spline
# All rights reserved.
#
#
###

import supybot.conf as conf
import supybot.registry as registry
try:
    from supybot.i18n import PluginInternationalization
    _ = PluginInternationalization('NFLDraft')
except:
    # Placeholder that allows to run the plugin on a bot
    # without the i18n module
    _ = lambda x:x

def configure(advanced):
    # This will be called by supybot to configure this module.  advanced is
    # a bool that specifies whether the user identified himself as an advanced
    # user or not.  You should effect your configuration by manipulating the
    # registry as appropriate.
    from supybot.questions import expect, anything, something, yn
    conf.registerPlugin('NFLDraft', True)


NFLDraft = conf.registerPlugin('NFLDraft')
conf.registerGlobalValue(NFLDraft, 'logURLs', registry.Boolean(False, """Should we log all URL calls?"""))
conf.registerGlobalValue(NFLDraft, 'checkInterval', registry.NonNegativeInteger(10, """Positive Integer in seconds to check."""))

# vim:set shiftwidth=4 tabstop=4 expandtab textwidth=79:
