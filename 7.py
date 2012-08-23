#http://www.pythonchallenge.com/pc/def/oxygen.html
import urllib, os
import Image, ImageDraw

url = 'http://www.pythonchallenge.com/pc/def/oxygen.png'
image_filename = urllib.urlretrieve(url, url.split('/')[-1])[0]

image = Image.open(image_filename)
w,h = image.size
print ''.join(chr(image.getpixel((i, h/2))[0]) for i in range(0,w,7))


tmp = [105, 110, 116, 101, 103, 114, 105, 116, 121]
print ''.join(chr(each) for each in tmp)
