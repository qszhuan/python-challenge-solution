#http://www.pythonchallenge.com/pc/return/mozart.html
import Image

image = Image.open('mozart.gif')

w,h = image.size
print w,h
def get_locator():
    for row in range(h):
        for col in range(w-5):
            if image.getpixel((col, row)) == image.getpixel((col+4, row)) == 195:
                yield (row, col)

list = get_locator()
result = Image.new(image.mode, (w*2, h))
for row_loc, col_loc in list:
    for i in range(w):
        result.putpixel((i + w-col_loc,row_loc), image.getpixel((i, row_loc)))
    
result.save('mozart_result.gif')
