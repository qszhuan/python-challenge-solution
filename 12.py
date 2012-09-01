#http://www.pythonchallenge.com/pc/return/evil1.jpg

# => http://www.pythonchallenge.com/pc/return/evil2.jpg

# not jpg, _.gfx

# => http://www.pythonchallenge.com/pc/return/evil2.gfx

import urllib

gfx = urllib.urlretrieve('http://huge:file@www.pythonchallenge.com/pc/return/evil2.gfx', 'evil2.gfx')[0]

data = open(gfx).read()

[open('%d.jpeg' % i, 'w').write(data[i::5]) for i in range(5)]

#disproportionality without ity

# => http://www.pythonchallenge.com/pc/return/evil3.jpg
# => http://www.pythonchallenge.com/pc/return/evil4.jpg =>txt file
