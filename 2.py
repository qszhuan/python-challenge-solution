#http://www.pythonchallenge.com/pc/def/ocr.html
import urllib2
import string

resp = urllib2.urlopen('http://www.pythonchallenge.com/pc/def/ocr.html').read()
start_index = resp.rindex('<!--')
#print ''.join(letter for letter in resp[start_index+4:-3] if letter.isalpha())
print resp[start_index+4:-3].translate(None, string.punctuation+string.whitespace)
