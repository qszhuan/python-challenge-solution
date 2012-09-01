#! /Users/zhuanqingshan/virtual_env/datawinners/bin/python
import os, sys
cur_file_dir= sys.path[0]
print open(os.path.join(cur_file_dir, 'readme.txt')).read()
