#http://www.pythonchallenge.com/pc/return/evil1.jpg

# => http://www.pythonchallenge.com/pc/return/evil2.jpg

# not jpg, _.gfx

# => http://www.pythonchallenge.com/pc/return/evil2.gfx

import urllib

gfx = urllib.urlretrieve('http://huge:file@www.pythonchallenge.com/pc/return/evil2.gfx', 'evil2.gfx')[0]

data = open(gfx).read()

f1 = open('1.jpeg', 'w')
f2 = open('2.jpeg', 'w')
f3 = open('3.jpeg', 'w')
f4 = open('4.jpeg', 'w')
f5 = open('5.jpeg', 'w')
f1.write(data[::5])
f2.write(data[1::5]) 
f3.write(data[2::5])
f4.write(data[3::5])
f5.write(data[4::5])

#disproportionality without ity
