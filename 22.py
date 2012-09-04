#http://www.pythonchallenge.com/pc/hex/copper.html
#http://www.pythonchallenge.com/pc/hex/white.gif

import Image, ImageSequence
import urllib

#urllib.urlretrieve('http://butter:fly@www.pythonchallenge.com/pc/hex/white.gif', 'white.gif')

image = Image.open('white.gif')
#### SUMMARY ####
print image.size
print image.info
print image.getbbox()
print image.getcolors()

### get all frames 's bbox ####
def getbboxes():
    for frame in ImageSequence.Iterator(image):
        yield frame.getbbox()[0:2]

result = list(getbboxes())
print result.count((100, 100))

##### split by item #######
def getsub(seq, item):
    result = []
    for each in seq:
        if each == item and result:
            yield result 
            result = []
        result.append(each)
    yield result

import pprint
pprint.pprint(list(getsub(result, (100,100))))

#draw characters
import numpy
index = 0
for each in getsub(result, (100,100)):
    im = Image.new(image.mode,image.size,0)
    start = (100, 100)
    for point in each:
        im.putpixel(start, 255)
        start = (numpy.array(point)-numpy.array((100,100)) + numpy.array(start)).tolist()
    im.save('white_%d.gif' % index)
    index = index + 1

### test for getsub ####
import unittest

class TestGetSub(unittest.TestCase):
    def test_getsub(self):
        test = ['a','b','a','b','c','a','a']
        results = list(getsub(test, 'a'))
        print results
        self.assertEqual(4, len(results))
        self.assertEqual([['a','b'],['a','b','c'],['a'],['a']], results)
