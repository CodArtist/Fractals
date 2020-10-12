import turtle

bob =turtle.Turtle()
bob.speed(100000)
bob.penup()
bob.forward(-150)
bob.pendown()
color = ["green","blue","red"]
i=0

def star(turtle,size,col):
    
    if size <=10:
    	return
    else:
        turtle.fillcolor(col)
        turtle.begin_fill()
        for i in range(4):       
           turtle.forward(size)
           star(bob,size/2,col)
           turtle.left(90)
        turtle.end_fill()
        

star(bob,250,color[0])
turtle.done()