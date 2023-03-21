import turtle

# Create a Turtle screen
screen = turtle.Screen()

# Create a Turtle pen
pen = turtle.Turtle()

pen.penup()
pen.goto(50, 50)
pen.pendown()

# Draw a circle with radius 50
pen.circle(300)

# Keep the screen open until closed manually
screen.mainloop()
