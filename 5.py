#http://www.pythonchallenge.com/pc/def/peak.html
import urllib2
import pickle

url = 'http://www.pythonchallenge.com/pc/def/banner.p'
peakhell = urllib2.urlopen(url)
data = pickle.load(peakhell)

for row in data:
    print(''.join(each[0]*each[1] for each in row))
