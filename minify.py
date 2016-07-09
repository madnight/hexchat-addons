__module_name__ = "URL Shortener" 
__module_version__ = "1.0.1" 
__module_description__ = "Parses given text for URLs and shortens them using is.gd"
__module_author__ = "Lacer <lacer.dragon(at)hotmail.com>, Fabian Beuke <mail(at)beuke.org>"

import hexchat, re
from pyshorteners.shorteners  import Shortener

def minify_callback (word, word_eol, userdata):
    if len(word) < 2:
        return hexchat.EAT_ALL
    
    shorty = Shortener('Isgd')
    words = word_eol[1].split()
    finalwords = ''
    for w in words:
        if is_url(w): # abstracted this out incase I want to replace it
            w = shorty.short(w) # shrink that bitch
        finalwords = finalwords + w + ' ' # append each word changed or otherwise back into the sentence
        
    currentchannel = hexchat.get_info('channel')
    hexchat.command("MSG  " + currentchannel + " " + finalwords)
    return hexchat.EAT_ALL
    
def is_url(s):
    # This blob of unholy hatred is from http://stackoverflow.com/questions/6883049/regex-to-find-urls-in-string-in-python
    url_regex ='http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
    if re.search(url_regex, s) == None:
        return False
    return True

# Channel hook
hexchat.hook_print("Your Message", minify_callback)
# Script load message
hexchat.prnt("URL Shortener loaded!")
