#http://www.pythonchallenge.com/pc/def/channel.html

import urllib,os
import zipfile

url = 'http://www.pythonchallenge.com/pc/def/channel.zip'

filename = 'channel.zip'
file = filename if os.path.exists(filename) else urllib.urlretrieve(url, url.split('/')[-1])[0]

zf  = zipfile.ZipFile(file)

for fn in zf.filelist:
 print zf.read(fn)


def get():
    idx = '90052'
    while True:
        fn = idx + '.txt'
        yield zf.getinfo(fn).comment
        idx = zf.read(fn).split()[-1]
        if not idx.isdigit():  break

print ''.join(get())
