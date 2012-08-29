#http://www.pythonchallenge.com/pc/hex/bin.html
import urllib2

auth_handler = urllib2.HTTPBasicAuthHandler()
auth_handler.add_password('pluses and minuses', 'www.pythonchallenge.com', 'butter', 'fly')
opener = urllib2.build_opener(auth_handler)
urllib2.install_opener(opener)

f = urllib2.urlopen('http://www.pythonchallenge.com/pc/hex/bin.html')
data = f.readlines()
print len(data)

encoded = ''.join(data[27:-4])

import base64

dec = base64.decodestring(encoded)
f = open('indian.wav', 'wb')
f.write(dec)
