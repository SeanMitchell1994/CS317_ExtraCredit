from turtle import *
from tail_recursion import tail_recursive, recurse
import colorsys
import turtle
import time

#color('#0099e6','white')
turtle.speed(0)
#begin_fill()
color_lut = []

@tail_recursive
def quarter_circle(steps,length,side,base_color):

	if (steps <= 0):
		return

	if (side == 1):
		# color = colorsys.hsv_to_rgb(((steps*side)+550)/1000, 1.0, 1.0)
		turtle.color(color_lut[base_color - (steps) + 90])
	elif (side == -1):
		turtle.color(color_lut[base_color + (steps)])

	turtle.forward(1)
	turtle.right(-1)
	quarter_circle(steps-1,length,side,base_color)

@tail_recursive
def inner_circle(steps):
	if (steps <= 0):
		return

	#pencolor(colors[i % 3])
	quarter_circle(90,1,1,700)
	turtle.right(270)
	quarter_circle(90,1,-1,700)
	right(5)
	inner_circle(steps-1)

@tail_recursive
def petal_ring(steps):
	if (steps <= 0):
	    	return

	quarter_circle(90,1,1,790)
	turtle.right(270)
	quarter_circle(90,1,-1,790)
	forward(9)
	#right(-90)
	#right(6)
	right(-84)
	petal_ring(steps-1)

def Main():
	start = time.time()
	for i in range(1000):
		color_lut.append(colorsys.hsv_to_rgb(i/1000, 1.0, 1.0))

	pensize(2)
	bgcolor('black')
	hideturtle()
	color(color_lut[700 + 90])
	circle(85)
	up()
	setpos(0, 85)
	down()
	speed(0)

	inner_circle(19)

	color(color_lut[700+90+90])
	up()
	setpos(-15,-75)
	down()
	circle(160)

	color(color_lut[550 + 90 + 90+90])
	up()
	setpos(-25, -145)
	down()
	circle(235)

	up()
	setheading(0)
	setpos(85,90)
	down()
	petal_ring(60)
	end = time.time()
	print(end - start)
	done()

Main()
#end_fill()
done()
