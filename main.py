import turtle
import random
import colorgram
from turtle import Turtle

# Create a turtle named 'timmy'
timmy = Turtle()
timmy.shape("turtle")

# Create an empty list to store colors extracted from an image
color_list = []

# Create a turtle screen
screen = turtle.Screen()

# Set initial position for the turtle to the leftmost bottom side
square_size = 100
timmy.penup()
timmy.goto(-screen.window_width() / 2 + square_size / 2, -screen.window_height() / 2 + square_size / 2)
timmy.pendown()
timmy.speed("fastest")
# Calculate the maximum x-coordinate for the turtle to move before wrapping to the next row
max_x = screen.window_width() / 2 - square_size / 2


# Function to extract colors from an image and store them in the color_list
def extract_color():
    colors = colorgram.extract('colorgrams/image.jpg', 100)
    for color in colors:
        # Check if the turtle's x-coordinate exceeds the maximum x-coordinate
        if timmy.xcor() > max_x:
            # Move the turtle to the start of the next row
            timmy.penup()
            timmy.goto(-screen.window_width() / 2 + square_size / 2, timmy.ycor() - square_size - 10)
            timmy.pendown()

        # Append normalized RGB values to the color_list
        color_list.append((color.rgb.r/255, color.rgb.g/255, color.rgb.b/255))
    return color_list


# Call the function to extract colors and store them in list_of_colors
list_of_colors = extract_color()

# Loop to create a pattern using dots with random colors
for i in range(len(list_of_colors)//2):
    for j in range(len(list_of_colors) // 2):
        timmy.pendown()
        # Draw a dot with a random color from the list
        timmy.dot(20, random.choice(list_of_colors))
        # Move the turtle forward by 50 units
        timmy.penup()
        timmy.forward(50)

    # Adjust the turtle's position based on the row index
    if i % 2 == 0:
        timmy.left(90)
        timmy.forward(30)
        timmy.left(90)
    else:
        timmy.right(90)
        timmy.forward(30)
        timmy.right(90)

# Close the turtle screen on click
screen.exitonclick()
