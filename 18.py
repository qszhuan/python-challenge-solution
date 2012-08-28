#http://www.pythonchallenge.com/pc/return/balloons.html

# say: brightness
# => <!-- maybe consider deltas.gz -->

import urllib

#urllib.urlretrieve('http://huge:file@www.pythonchallenge.com/pc/return/deltas.gz','deltas.gz')

import gzip

gz_file = gzip.GzipFile('deltas.gz')
lines = gz_file.read().split('\n')
pairs =  [line.rpartition('   ')[::2] for line in lines]
columns = [[p[i] for p in pairs] for i in range(2)]

import difflib
diffs = difflib.Differ().compare(columns[0], columns[1])
import pprint
pprint.pprint(list(diffs))

pngs = [''.join(filter(lambda l: l[0] == d, diffs)) for d in " -+"]
print pngs
import codecs, re
def unhex(s): 
    return codecs.getdecoder('hex')(re.sub('[^0-9a-fA-F]', '', s))[0]

for i in range(len(pngs)): open('delta%d.png' % (i + 2), 'wb').write(unhex(pngs[i]))
