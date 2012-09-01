#http://www.pythonchallenge.com/pc/return/romance.html
import urllib2, cookielib

auth_handler = urllib2.HTTPBasicAuthHandler()
auth_handler.add_password('inflate', 'www.pythonchallenge.com', 'huge', 'file')
cj = cookielib.CookieJar()
cookie_handler = urllib2.HTTPCookieProcessor(cj)
opener = urllib2.build_opener(auth_handler, cookie_handler)
urllib2.install_opener(opener)

h = opener.open('http://www.pythonchallenge.com/pc/return/romance.html')
#resp = urllib2.urlopen('http://www.pythonchallenge.com/pc/return/romance.html')
print list(cj)

start = '12345'
h = opener.open('http://www.pythonchallenge.com/pc/def/linkedlist.php?busynothing=%s' % start)
print list(cj)

import re
result = []
def get_cookie(index, result):
    text = opener.open('http://www.pythonchallenge.com/pc/def/linkedlist.php?busynothing=%s'%index).read()
    match = re.search('and the next busynothing is (\d+)', text)
    result.append(list(cj)[0].value)
    if match:
        return match.group(1)
    else:
        print text
        return None

while True:
    start = get_cookie(start, result)
    if not start:
        print 'stopped'
        break

    print start
message = ''.join(result)
print message

import bz2,urllib
    
print bz2.decompress(urllib.unquote_plus(message))

#'is it the 26th already? call his father and inform him that "the flowers are on their way". he\'ll understand.'

#mozart's father: Leopold
#call him: level 13
# => 555-VIOLIN
import xmlrpclib                                                               
server = xmlrpclib.Server('http://www.pythonchallenge.com/pc/phonebook.php')   
print server.phone('Leopold')                                                     
                                                                               
                                                                               
