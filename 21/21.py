#! /Users/zhuanqingshan/virtual_env/datawinners/bin/python
############## get data #############
import os, sys
cur_file_dir= sys.path[0]
print open(os.path.join(cur_file_dir, 'readme.txt')).read()

f = open(os.path.join(cur_file_dir, 'package.pack'))
data = f.read()

########### hex lookup #############
import codecs
print codecs.encode(data[:20], 'hex')

########## start ################
import zlib, bz2
sample = zlib.decompress(data)[:20]
print sample

log = []

def logger(fn):
    def _logger(d):
        global log
        if d[:2] == 'x\x9c': log.append('z')
        elif d[:2] == 'BZ':  log.append('b')
        elif d[-2:] == '\x9cx':  log.append('Z')
        elif d[-2:] == 'ZB':  log.append('B')
        return fn(d)
    return _logger

@logger
def uncompress(data):
    if data[:2] == 'x\x9c': return zlib.decompress(data);
    elif data[:2] == 'BZ': return bz2.BZ2Decompressor().decompress(data)
    elif data[-2:] == '\x9cx': return zlib.decompress(data[::-1])
    elif data[-2:] == 'ZB': return bze.BZ2Decompressor().decompress(data[::-1])
    else: return None

while True:
    ret =  uncompress(data)
    if ret is None: break
    data = ret
print data[::-1]

import pprint
pprint.pprint( ''.join(log).split('Z'))
