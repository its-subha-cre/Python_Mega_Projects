import turtle
def func():
    turtle.hideturtle()
    turtle.up()
    turtle.goto(-100,-400)
    turtle.down()
    turtle.left(90)
    turtle.forward(650)
    turtle.color("red")
    turtle.begin_fill()
    turtle.right(90)
    turtle.forward(300)
    turtle.right(90)
    turtle.forward(80)
    turtle.right(90)
    turtle.forward(300)
    turtle.end_fill()

    turtle.color("#00008B")
    turtle.begin_fill()
    turtle.bk(300)
    turtle.left(90)
    turtle.forward(80)
    turtle.right(90)
    turtle.forward(300)
    turtle.end_fill()

    turtle.color("#FFA500")
    turtle.begin_fill()
    turtle.bk(300)
    turtle.left(90)
    turtle.forward(80)
    turtle.right(90)
    turtle.forward(300)
    turtle.end_fill()

    turtle.up()
    turtle.goto(100,-100)
    turtle.down()
    turtle.write("Armenia",font=("Arial Black",21,"normal"))

    # if __name__=="__main__":
func()
turtle.done()
   