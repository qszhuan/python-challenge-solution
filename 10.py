#view-source:http://www.pythonchallenge.com/pc/return/bull.html

# a = [1, 11, 21, 1211, 111221, 
# len(a[30]) = ?

index = 0
start = '1'
while index <= 30:
    print index, len(start)
    next = []
    for each in start:
        if next and  next[-1][0] == each:
            next[-1][1] = next[-1][1] + 1
        else:
            next.append([each, 1])
    start =  ''.join(str(count)+str(num) for num, count in next)
    index = index + 1    
