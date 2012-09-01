#http://www.pythonchallenge.com/pc/def/equality.html
import urllib2
import re

resp = urllib2.urlopen('http://www.pythonchallenge.com/pc/def/equality.html').read()
start_index = resp.rindex('<!--')

print ''.join(re.findall('[^A-Z][A-Z]{3}([a-z])[A-Z]{3}[^A-Z]', resp[start_index:]))
