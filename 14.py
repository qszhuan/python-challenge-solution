#http://www.pythonchallenge.com/pc/return/italy.html
import Image, urllib

class Walker(object):
    ROTATES = ['CW', 'CWW']
    SCREW = ['IN','OUT']
    def __init__(self,row = 100, col = 100, rotates =  'CCW', screw = 'OUT'):
        self.route = {'R': (0,1), 'D': (1,0), 'L':(0,-1), 'U':(-1, 0)}
        self.clear(row, col)
        self.direction = ['R','D','L','U']
        if rotates == 'CW':
            self.cur_direct = self.direction[0]
            self.turn = self.turn_right
        elif rotates == 'CCW':
            self.cur_direct = self.direction[1]
            self.turn = self.turn_left
        else:
            raise
        if screw == 'OUT':
            self.i, self.j = row/2, col/2
            self.move = self.screw_out
            self.step_limit = 1
            self.turned = False
            self.moved_times = 0
        elif screw == 'IN':
            self.i, self.j = 0, 0
            self.move = self.screw_in

    def turn_right(self):
        print "Turn Right"
        self.cur_direct = self.direction[(self.direction.index(self.cur_direct) + 1)% len(self.direction)] 
        return self.route[self.cur_direct]

    def turn_left(self):
        print "Turn Left"
        self.cur_direct = self.direction[(self.direction.index(self.cur_direct) + 3)% len(self.direction)] 
        return self.route[self.cur_direct]

    def clear(self, row, col):
        self._map = [[]]*row
        for x in range(row):
            self._map[x] = [False]*col
        
    def screw_in(self):
        x,y = self.route[self.cur_direct]
        if self._map[self.i][self.j] is False:
            pass
        elif (0 <= self.i + x < len(self._map[0]) and 0 <= self.j + y < len(self._map)) and  not self._map[self.i+x][self.j+y]:
            self.i,self.j = self.i + x, self.j + y
        else:
            self.turn()
            x,y = self.route[self.cur_direct]
            self.i, self.j = self.i + x, self.j + y
            if self._map[self.i][self.j] == True: return None
        
        self._map[self.i][self.j] = True
        return (self.i, self.j)

    def screw_out(self):

        if self._map[self.i][self.j] is False:
            self._map[self.i][self.j] = True
            return (self.i, self.j)
        elif self.turned and self.moved_times >= self.step_limit:
            self.step_limit = self.step_limit + 1
            self.turned = False
            self.turn()
            self.moved_times = 0
        elif self.moved_times >= self.step_limit:
            self.turned = True
            self.turn()
            self.moved_times = 0
        self.moved_times = self.moved_times + 1
        x,y = self.route[self.cur_direct]
        self.i, self.j = self.i + x, self.j + y        
        if not (0 <= self.i < len(self._map[0]) and 0 <= self.j < len(self._map)) or self._map[self.i][self.j] == True :
            return None
        self._map[self.i][self.j] = True
        return (self.i, self.j)
        
##########################################################################################
#urllib.urlretrieve('http://www.pythonchallenge.com/pc/return/wire.png', 'wire.png')

#walker = Walker(3,3)
#src = [[1,2,3],[4,5,6],[7,8,9]]
#dest = []
#while True:
#    pos = walker.move()
#    if not pos:
#        print 'End'
#        break
#    dest.append(src[pos[0]][pos[1]])
#print dest
#exit()
image = Image.open('wire.png')
result = Image.new(image.mode, (100,100))
walker = Walker(rotates='CW', screw="IN")
index = 0

while True:
    pos = walker.move()
    if not pos:
        print "End"
        break
    print pos
    result.putpixel(pos, image.getpixel((index,0)))
    index = index + 1

result.save('result.png')
