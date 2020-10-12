import turtle
bob = turtle.Turtle()
bob.speed(1000)
bob.penup()
bob.goto(30,50)
bob.pendown()
def spiral(turtle,size):
	for k in range(2):
		for i in range(100):
			turtle.forward(size)
			turtle.left(i)
		turtle.penup()
		turtle.goto(30,50)
		turtle.pendown()
		turtle.left(220)
		for i in range(50):
			turtle.forward(size)
			turtle.right(i)
		turtle.penup()
		turtle.goto(30,50)
		turtle.pendown()
		turtle.setheading(180)
y=1
for m in range(1,80,2*y):
	spiral(bob,m)
	bob.left(180)
	y=2*y
turtle.done()
