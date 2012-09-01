#http://www.pythonchallenge.com/pc/hex/idiot2.html
import re
import httplib
import base64

def get_response(page, start):
    print page, start
    headers = {'Authorization': 'Basic ' + base64.b64encode('butter:fly'),
               'Range' : 'bytes=%d-' % (start, )}
    conn = httplib.HTTPConnection('www.pythonchallenge.com')
    print headers
    conn.request('GET', page, '', headers)
    resp= conn.getresponse()
    return resp
#r = get_response('/pc/hex/unreal.jpg',30203,30300)
#print r.getheaders()
#print r.read()
#exit()
def next_range(start, starts, results):
    response = get_response('/pc/hex/unreal.jpg', start)
    starts.append(start)
    results.append(response.read())
    m = re.match(r'bytes %d-(\d+)/2123456789' % start, response.getheader('Content-Range'))
    return int(m.group(1)) + 1

def decode():
    b = 30203
    starts = []
    results = []
    try:
        for i in range(400):
            b = next_range(b, starts, results)
    except:
        pass
    
    print results, starts
#decode()

def getdata(start):
    r = get_response('/pc/hex/unreal.jpg',start)
    print(r.getheaders())
    data = r.read()
    return data

data = getdata(2123456789) # #
print data                 # #
reverse_data = data[::-1]  # #
print reverse_data         # #
                           # #
data = getdata(2123456743) # #
print data                 # #
                           # #
data = getdata(1152983631) # #
print len(data)            # #
                           # #
print repr(data[:100])     # #

#################################################################################################################
# ########### Z I P ##############                                                                              #
# The zip file format was created by Phil Katz of PKWARE                                                        #
# Most of the signatures end with the short integer 0x4b50 (read as a little-endian number)                     #
# which when viewed as an ASCII string the hexadecimal 50 4B read "PK" the initials of the inventor Phil Katz.  #
# #This means when a ZIP file is viewed in a text editor the first two bytes of the file are "PK".              #
# # (A self-extracting ZIP has an EXE before the ZIP so would start with "MZ".)                                 #
# ########### Z I P ##############                                                                              #
#################################################################################################################

f = open('20.zip', 'wb') # #
f.write(data)            # #
f.close()                # #

import zipfile, StringIO                      
zf = zipfile.ZipFile('20.zip')
try: 
    zf.testzip() 
except Exception as e:
    print e.message

print zf.namelist()
zf.extractall(pwd='invader'[::-1])
