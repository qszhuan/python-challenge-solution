#http://www.pythonchallenge.com/pc/def/map.html
from string import maketrans, translate, ascii_lowercase

text = '''g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.'''

#table =  maketrans('abcdefghijklmnopqrstuvwxyz', 'cdefghijklmnopqrstuvwxyzab')
table = maketrans(ascii_lowercase, ascii_lowercase[2:]+ascii_lowercase[:2])
result = text.translate(table)
print result

print 'map'.translate(table)
