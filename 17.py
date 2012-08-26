#http://www.pythonchallenge.com/pc/return/romance.html
import urllib2, cookielib

auth_handler = urllib2.HTTPBasicAuthHandler()
auth_handler.add_password('inflate', 'www.pythonchallenge.com', 'huge', 'file')
cj = cookielib.CookieJar()
cookie_handler = urllib2.HTTPCookieProcessor(cj)
opener = urllib2.build_opener(auth_handler, cookie_handler)
urllib2.install_opener(opener)
opener.open('http://www.pythonchallenge.com/pc/return/romance.html')
#resp = urllib2.urlopen('http://www.pythonchallenge.com/pc/return/romance.html')
print list(cj)
