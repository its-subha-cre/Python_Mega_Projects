
from turtle import *
speed(0)
ht()
setup(width=1000,height=600)
bgcolor('red')

def star(size):
    color('yellow')
    begin_fill()
    for i in range(0,5):
        # color('yellow')
        # begin_fill()
        fd(size)
        rt(144)
        # end_fill()
    end_fill()
#Just trial and erroring for the position of the 5 star:
pu()
goto(-420,200)
pd()
star(150)
pu()
fd(200)
lt(90)
fd(75)
pd()
rt(110)
star(50)
lt(20)
pu()
fd(100)
rt(90)
fd(100)
pd()
rt(110)
star(50)
lt(110)
pu()
fd(55)
rt(90)
fd(50)
lt(180)
pd()
star(50)
pu()
bk(60)
rt(90)
fd(50)
lt(70)
pd()
star(50)
done()