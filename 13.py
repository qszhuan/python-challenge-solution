#http://www.pythonchallenge.com/pc/return/disproportional.html

import Image, ImageDraw
import urllib

image_url = 'http://huge:file@www.pythonchallenge.com/pc/return/disprop.jpg'

urllib.urlretrieve(image_url, 'disprop.jpg')

coords = 326,177,45

image = Image.open('disprop.jpg')
draw = ImageDraw.Draw(image)
draw.ellipse((326-45, 177-45, 326+45, 177+45))
image.save('result.jpg')

# => 5

phonebook_url = 'http://huge:file@www.pythonchallenge.com/pc/phonebook.php'
urllib.urlretrieve(phonebook_url, 'phonebook.php')

