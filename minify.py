__module_name__ = "URL Shortener" 
__module_version__ = "1.0.1" 
__module_description__ = "Parses given text for URLs and shortens them using is.gd"
__module_author__ = "Lacer <lacer.dragon(at)hotmail.com>, Fabian Beuke <mail(at)beuke.org>"

import hexchat, validators
from pyshorteners.shorteners import Shortener

# Documentation about Python Hexchat Hooks
# http://hexchat.readthedocs.io/en/latest/script_python.html

def minify_callback(word, word_eol, userdata):
    shorty = Shortener('Isgd')
    words = word_eol[0].split() # word_eol[0] is the full text message
    finalwords = ''
    for word in words:
        if validators.url(word):
            word = shorty.short(word)
        finalwords += word + ' ' 
    currentchannel = hexchat.get_info('channel')
    hexchat.command("MSG  " + currentchannel + " " + finalwords)
    return hexchat.EAT_ALL

# empty string hook to capture every message a user sends
hexchat.hook_command("min", minify_callback)
hexchat.prnt("URL Shortener Version " + __module_version__ + " loaded!")
