# uncompyle6 version 3.7.4
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.8.2 (default, Jul 16 2020, 14:00:26) 
# [GCC 9.3.0]
# Embedded file name: /usr/lib/enigma2/python/Plugins/Extensions/MeoBoot/__init__.py
# Compiled at: 2014-02-10 23:23:49
from Components.Language import language
from Tools.Directories import resolveFilename, SCOPE_PLUGINS, SCOPE_LANGUAGE
import os, gettext
PluginLanguageDomain = 'MeoBoot'
PluginLanguagePath = 'Extensions/MeoBoot/po'

def localeInit():
    lang = language.getLanguage()[:2]
    os.environ['LANGUAGE'] = lang
    print '[MeoBoot] set language to ', lang
    gettext.bindtextdomain(PluginLanguageDomain, resolveFilename(SCOPE_PLUGINS, PluginLanguagePath))


def _(txt):
    t = gettext.dgettext(PluginLanguageDomain, txt)
    if t == txt:
        print '[MeoBoot] fallback to default translation for', txt
        t = gettext.dgettext('enigma2', txt)
    return t


localeInit()
language.addCallback(localeInit)
# okay decompiling __init__.pyo
