import turtle

# Set the background color
turtle.bgcolor("black")

# Set the turtle's shape
turtle.shape("turtle")

# Set the turtle's speed
turtle.speed(10)

# Set the turtle's color
turtle.color("red")

# Set the pen size
turtle.pensize(5)

# Move the turtle to the starting position
turtle.penup()
turtle.goto(-200, 0)
turtle.pendown()

# Draw the head
turtle.circle(50)

# Draw the body
turtle.penup()
turtle.goto(-100, 0)
turtle.pendown()
turtle.forward(200)

# Draw the arms
turtle.penup()
turtle.goto(-150, 50)
turtle.pendown()
turtle.forward(100)

turtle.penup()
turtle.goto(-150, -50)
turtle.pendown()
turtle.forward(100)

# Draw the legs
turtle.penup()
turtle.goto(-100, -100)
turtle.pendown()
turtle.forward(100)

turtle.penup()
turtle.goto(-100, -50)
turtle.pendown()
turtle.forward(100)

# Keep the window open until it is closed
turtle.mainloop()