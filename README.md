# Hexchat Addons
[![Code Climate](https://codeclimate.com/github/madnight/hexchat-addons/badges/gpa.svg)](https://codeclimate.com/github/madnight/hexchat-addons)
[![Issue Count](https://codeclimate.com/github/madnight/hexchat-addons/badges/issue_count.svg)](https://codeclimate.com/github/madnight/hexchat-addons)

## Hexchat Url Shortenter
This is a hexchat script that turns your long link-laden chat lines into nice, concise sentences using the magic of the ethical URL shortening service is.gd.

### Example
   Before:
   
        These butterflies are so amazing! http://image.naldzgraphics.net/2011/04/1-dreams.jpg
   After:
   
       These butterflies are so amazing! http://is.gd/Bj5PNC

### Installation
    pip install pyshorteners validators
   http://hexchat.readthedocs.io/en/latest/faq.html#how-do-i-auto-load-scripts-at-startup
   
### Usage
        /min These butterflies are so amazing! http://image.naldzgraphics.net/2011/04/1-dreams.jpg

### Notes
   For chat messages containing multiple links, since each link involves accessing
   is.gd for shortening via their PHP interface, noticible lag will occur between 
   pressing enter and the final message being posted to the IRC server.

   Feel free to email me with messages about bad coding, cool butterflies, deals on viagra,
   or what your favorite Jolly Rancher flavor is. I probably wont read it.
   
## Hexchat Advanced Ignore
This script extens the normal IRC /ignore function by also ignoring the mentioning of the ignored nick.
### Example
   Before:
   
        IgnoreMe: These butterflies are so amazing!
        Nick123: IgnoreMe, cool!
   After:
         
         
         
### Usage
        /addignore IgnoreMe
        /delignore IgnoreMe

