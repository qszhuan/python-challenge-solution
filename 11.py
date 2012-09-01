#http://www.pythonchallenge.com/pc/return/5808.html
import urllib, Image

url = 'http://huge:file@www.pythonchallenge.com/pc/return/cave.jpg'

file_name = 'cave.jpg'#urllib.urlretrieve(url, 'cave.jpg')[0]

image = Image.open(file_name)
w, h = image.size
print w, h

odd = Image.new(image.mode, image.size)
odd.putdata(list(image.getdata())[1::2])
odd_file = open('odd.jpeg', 'w')
odd.save(odd_file)

