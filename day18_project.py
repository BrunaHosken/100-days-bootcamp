# Hirst Paiting Project

# import colorgram
import turtle as t
import random

# rgb_colors = []
# colors = colorgram.extract("hirst_spot_painting_image/image.jpg", 100)

# for color in colors:
#     r=color.rgb.r
#     g=color.rgb.g
#     b=color.rgb.b
#     new_color = (r,g,b)
#     rgb_colors.append(new_color)

# print(rgb_colors)

color_list = [ (236, 224, 80), (197, 7, 71), (195, 164, 13), (201, 75, 15), (231, 54, 132), (110, 179, 216), (217, 163, 101), (27, 105, 168), (35, 186, 109), (19, 29, 168), (13, 23, 66), (212, 135, 177), (233, 223, 7), (199, 33, 132), (13, 183, 212), (230, 166, 199), (126, 189, 162), (8, 49, 28), (40, 132, 77), (128, 219, 232), (58, 12, 25), (67, 22, 7), (114, 90, 210), (146, 216, 199), (179, 17, 8), (233, 66, 34), (11, 97, 52), (169, 181, 232), (241, 169, 155), (252, 7, 40), (10, 84, 100), (63, 98, 8), (14, 51, 250), (250, 11, 8)]

def random_color():
    color = random.choice(color_list)
    return color

t.colormode(255)
turtle = t.Turtle()
turtle.penup()
turtle.hideturtle() 
turtle.setheading(225)
turtle.forward(250)
turtle.setheading(0)



for _ in range (10):
    for _ in range(10):
        turtle.pendown()
        color = random_color()
        turtle.dot(20, color);
        turtle.penup()
        turtle.forward(50)
    turtle.setheading(90)
    turtle.forward(50)
    turtle.setheading(180)
    turtle.forward(500)
    turtle.setheading(0)    


screen = t.Screen()
screen.exitonclick()