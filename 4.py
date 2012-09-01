#http://www.pythonchallenge.com/pc/def/linkedlist.php
import urllib2

url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php/linkedlist.php?nothing=%s'

start = '12345'

while True:
    resp = urllib2.urlopen(url % start).read()
    print resp

    if resp == 'Yes. Divide by two and keep going.':
        start = str(int(start)/2)
        continue

    start = resp.split()[-1]
    if not start.isdigit():
        break
        
