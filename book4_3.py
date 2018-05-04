import turtle
import math


def square(t, length):
	"""T is a turtle
	"""
	for i in range(4):
		t.fd(length)
		t.lt(90)

def draw_square(t, length=100):
	square(t, length)


def polygon(t, n, length):
	"""T is a turtle, n is the number of sides
	"""
	angle = 360.0 / n
	polyline(t,n,length,angle)


def circle(t, radius):
	t.delay = 0.01 #make turtle go faster
	arc(t, radius, 360)


def arc(t, radius, angle):
	"""a more generalized version of circle

		angle: when angle is 360, a whole circle will be drawn 
	"""
	t.delay = 0.1
	factor = angle / 360.0
	circumference = 2 * math.pi * radius * factor
	n = int(circumference / 3) + 1
	length = circumference / n
	step_angle = angle*1.0/n
	# the following part is similar to polygon, so we should abstract a new function(polyline)
	# for i in range(n):
	# 	t.fd(length)
	# 	t.lt(angle * 1.0 / n)
	polyline(t, n, length, step_angle)

def polyline(t, n, length, angle):
	for i in range(n):
		t.fd(length)
		t.lt(angle)






def main():
	#draw_square(bob)
	
	bob = turtle.Turtle()
	#circle(bob, 60)
	#polygon(bob, n=7, length=70)
	arc(bob, radius=80, angle=180)

if __name__ == '__main__':
	main()
	turtle.mainloop()

