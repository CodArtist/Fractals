import turtle

bob =turtle.Turtle()
bob.speed(100)
def star(turtle,size):
    if size <=10:
    	return
    else:
        for i in range(5):
           turtle.forward(size)
           star(bob,size/3)
           turtle.left(216)
for i in range(5):
	star(bob,200)
	bob.penup()
	bob.forward(-300)
	bob.pendown()
turtle.done()