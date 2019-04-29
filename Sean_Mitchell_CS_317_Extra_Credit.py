# ====================================================
# Sean Mitchell
# CS 317-20 Spring 2019
# Extra Credit
#
# Creates a series of petals and rings using turtle
# The total shape as a color gradient that starts low
# and goes high as the shape size increases
# This base color is randomly chosen at runtime
#
# This version include tail_recursion.py
# ====================================================

from turtle import *
import colorsys
import time
from random import randint
from tail_recursion import tail_recursive, recurse		# tail_recursion.py is not mine, it's just an
														# interesting trick to speed up the program because
														# of sequential recurisive calls
														# Full credit is provided in the tail_recursion.py
														# The program runs fine without, it's just slower
														# With this added, it ran roughly 40% faster

color_lut = []											# color lookup table

@tail_recursive
def quarter_circle(steps,length,side,base_color):
	# steps = number of times to run
	# length = length to move forward
	# side = which side is the petal (coming or leaving origin?)
	# base_color = value of randomly chosen base color
	#
	# Draws a quarter circle

	# exit condition
	if (steps <= 0):
		return

	# determines if the petal is coming or leaving the origin
	if (side == 1):
		color(color_lut[base_color - (steps) + 90])
	elif (side == -1):
		color(color_lut[base_color + (steps)])

	# shifts by the value of the length
	forward(length)
	right(-length)

	# recursive call
	quarter_circle(steps-1,length,side,base_color)

@tail_recursive
def inner_circle(steps,base_color):
	# steps = number of times to run
	# base_color = value of randomly chosen base color
	#
	# Draws the inner geometry using quarter_circle()

	# exit condition
	if (steps <= 0):
		return

	# Draws a full petal
	quarter_circle(90,1,1,base_color)
	right(270)
	quarter_circle(90,1,-1,base_color)

	# shifts to the right by 5 pixels
	right(5)

	# recursive call
	inner_circle(steps-1,base_color)

@tail_recursive
def petal_ring(steps,base_color):
	# steps = number of times to run
	# base_color = value of randomly chosen base color
	#
	# Draws the outer geometry using quarter_circle()

	# exit condition
	if (steps <= 0):
	    	return

	# Draws a full petal
	quarter_circle(90,1,1,base_color+90)
	right(270)
	quarter_circle(90,1,-1,base_color+90)

	# shifts the position to follow the outline of the circle
	forward(9)
	right(-84)

	# recursive call
	petal_ring(steps-1,base_color)


def Main():
	start = time.time()

	# populates the color lookup table
	for i in range(1000):
		color_lut.append(colorsys.hsv_to_rgb(i/1000, 1.0, 1.0))

	# generates the random base color
	base_color = randint(0, 800)

	# run settings
	pensize(2)
	bgcolor('black')
	speed(0)
	hideturtle()

	# draws the first circle
	color(color_lut[base_color + 90])
	circle(85)
	up()
	setpos(0, 85)
	down()

	# draws the inner petals
	inner_circle(19,base_color)

	#draws the outer circle
	color(color_lut[base_color+180])
	up()
	setpos(-15,-75)
	down()
	circle(160)

	# draws the outer petals
	up()
	setheading(0)
	setpos(85,90)
	down()
	petal_ring(60,base_color)

	end = time.time()
	print(end - start)

	done()

Main()
