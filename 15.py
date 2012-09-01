#http://www.pythonchallenge.com/pc/return/uzi.html
import datetime
for i in range(0, 1000, 10):
    year = 1006 + i
    try:
        dt = datetime.datetime(year, 2, 29)
    except:
        pass
    else:
#        print dt
        today = datetime.date(year, 1, 26)
        if today.isoweekday() == 1:
            print "Today:", today
