import turtle 

spiral = turtle.Turtle()

for i in range(30):
    spiral.forward(i * 12)
    spiral.right(98)
    
turtle.done()