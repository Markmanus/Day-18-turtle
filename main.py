import turtle
from turtle import Turtle, Screen
import random

turtle.colormode(255)
tim = Turtle()

#colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
def random_color():
    r = random.randint(0,255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r,g,b)
    return random_color


tim.shape("turtle")


directions = 0
tim.speed(30)
tim.pensize(2)
for _ in range(200):
    tim.color(random_color())
    tim.setheading(directions)
    directions += 5
    tim.circle(100)



# def left():
#     tim.left(90)
#     tim.forward(20)
# def right():
#     tim.left(90)
#     tim.forward(20)
# def forward():
#     tim.forward(20)
# def backward():
#     tim.backward(20)
#
# options = [backward,forward,left,right]
# for i in range(10):
#     random_function = random.choice(options)
#     random_function()


#second challenge








##first challange
# corner = 50
# turn = 360
# degree = int(turn / corner)
#
# print(degree)
# def draw_shape(num_sides):
#     angle = 360 / num_sides
#     for i in range(num_sides):
#         tim.forward(100)
#         tim.right(angle)
#
# for shape_side_n in range(3,11):
#     tim.color(random.choice(colours))
#     draw_shape(shape_side_n)
# # tim.right(90)
# # tim.forward(50)
# # tim.right(90)
# # tim.forward(50)
# # tim.right(90)
# # tim.forward(50)












screen = Screen()
screen.exitonclick()