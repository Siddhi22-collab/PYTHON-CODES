import turtle

# Create turtle object
pen = turtle.Turtle()

# Set speed
pen.speed(3)

# Set color
pen.color("red")

# Start drawing heart
pen.begin_fill()

pen.left(140)
pen.forward(180)

pen.circle(-90, 200)
pen.left(120)
pen.circle(-90, 200)

pen.forward(180)

pen.end_fill()

# Hide turtle
pen.hideturtle()

# Keep window open
turtle.done()