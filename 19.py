#http://www.pythonchallenge.com/pc/hex/bin.html
import urllib2

auth_handler = urllib2.HTTPBasicAuthHandler()
auth_handler.add_password('pluses and minuses', 'www.pythonchallenge.com', 'butter', 'fly')
opener = urllib2.build_opener(auth_handler)
urllib2.install_opener(opener)

f = urllib2.urlopen('http://www.pythonchallenge.com/pc/hex/bin.html')
data = f.readlines()
print len(data)

encoded = ''.join(data[27:-4])

import base64

dec = base64.decodestring(encoded)
f = open('indian.wav', 'wb')
f.write(dec)

import wave
iw = wave.open('indian.wav')
frames = iw.readframes(iw.getnframes())
print frames[:40]

iw2 = wave.open('indian2.wav', 'w')
iw2.setnchannels(1)
iw2.setsampwidth(iw.getsampwidth())
iw2.setframerate(iw.getframerate()//2)
iw2.writeframes(frames[::2])
iw2.close()
iw.close()
