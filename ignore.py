import hexchat, re

__module_name__ = "Ignores IRC People"
__module_author__ = "madnight"
__module_version__ = "0.0.1"
__module_description__ = "Ignores IRC People and their mentioning"

ignorelist = []

def loadlist():
    global ignorelist
    try:
        ignorelist = hexchat.get_pluginpref('ignorelist').split(',')
    except: pass

def savelist():
    global ignorelist
    ignorelist = filter(None, ignorelist)
    hexchat.set_pluginpref('ignorelist', ','.join(ignorelist))
    loadlist()
    printlist()

def ignore(word, word_eol, userdata):
    global ignorelist
    for nick in ignorelist:
        if not nick:
            return hexchat.EAT_ALL
        # word_eol[0] contains nick an msg
        if re.search(nick +'[,:\s]', word_eol[0]) is not None: 
            return hexchat.EAT_ALL

def addignore(word, word_eol, userdata):
    global ignorelist
    ignorelist.append(word[1])
    savelist()
    return hexchat.EAT_ALL

def delignore(word, word_eol, userdata):
    global ignorelist
    try:
        ignorelist.remove(word[1])
        savelist()
    except: pass
    return hexchat.EAT_ALL

def printlist():
    global ignorelist
    if len(ignorelist) == 0:
        hexchat.prnt('Ignorelist is empty')
        return
    hexchat.prnt('Ignorelist: ' + ' '.join(ignorelist))

loadlist()
hexchat.hook_print("Channel Message", ignore, "Channel Message")
hexchat.hook_print("Channel Msg Hilight", ignore, "Channel Msg Hilight")
hexchat.hook_command("addignore", addignore)
hexchat.hook_command("delignore", delignore)
hexchat.prnt(__module_name__ + " " + __module_version__ + " loaded!")
printlist()
