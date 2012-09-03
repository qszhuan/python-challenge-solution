#! /Users/zhuanqingshan/virtual_env/datawinners/bin/python
import os, sys
cur_file_dir= sys.path[0]
print open(os.path.join(cur_file_dir, 'readme.txt')).read()

f = open(os.path.join(cur_file_dir, 'package.pack'))
data = f.read()

import codecs
print codecs.encode(data[:20], 'hex')

import zlib
sample = zlib.decompress(data)[:20]

