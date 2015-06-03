__module_name__ = "URL Shortener" 
__module_version__ = "1.0" 
__module_description__ = "Parses given text for URLs and shortens them using is.gd"
__module_author__ = "Lacer <lacer.dragon(at)hotmail.com>"

# README
#   This is a hexchat script that turns your long link-laden chat lines into
#   nice, concise sentences using the magic of the ethical URL shortening service
#   is.gd. It only works when invoked with the /min command on lines containing 
#   valid HTTP URLs.
#
# EXAMPLE
#   Before:
#       /min These butterflies are so amazing! http://image.naldzgraphics.net/2011/04/1-dreams.jpg http://www.pingleton.com/field/peru/day14/P1070927.JPG
#   After:
#       These butterflies are so amazing! http://is.gd/Bj5PNC http://is.gd/EnHgIC
#
# INSTALL
#   This script requires the pyshorteners library which can be easily downloaded 
#   from the cheeseshop @ https://pypi.python.org/pypi/pyshorteners/ and installed
#   using $ python setup.py install
#   or it can be directly downloaded/installed using $ pip install pyshorteners

# NOTES
#   For chat messages containing multiple links, since each link involves accessing
#   is.gd for shortening via their PHP interface, noticible lag will occur between 
#   pressing enter and the final message being posted to the IRC server.
#   I'll probably make another script that uses imgur's API to make a gallery of
#   links in a message but until then, this will have to do.

#  Feel free to email me with messages about bad coding, cool butterflies, deals on viagra,
#  or what your favorite Jolly Rancher flavor is. I probably wont read it.


import hexchat, re
from pyshorteners.shorteners  import Shortener

def minify_callback (word, word_eol, userdata):
    if len(word) < 2:
        hexchat.prnt("Usage: /min Text containing links http://to.be shortened.")
        return hexchat.EAT_ALL
    
    shorty = Shortener('IsgdShortener')
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

# Channel hook to listen for the /ap invocation
hexchat.hook_command("min", minify_callback, help="Usage: /min Text containing links http://to.be shortened.")
# Script load message
hexchat.prnt("URL Shortener loaded! Usage: /min Text containing links http://to.be shortened. Will lag with multiple URLs!")