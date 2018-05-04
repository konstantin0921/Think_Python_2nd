import turtle
import math

def isosceles(t, angle, twist):
	"""Draws an isosceles triangle.

	t: Turtle
	angle: peak angle in degrees
	twist: length of the equal twist

	"""
	y = math.sin(angle * math.pi / 180) * twist

	t.rt(angle)
	t.fd(twist)
	t.lt(90+angle)
	t.fd(2*y)
	t.lt(90+angle)
	t.fd(twist)
	t.lt(180-angle)

def polygon_triangle(t, n, radius):
	"""Draws an polygon built up with multiple isosceles triangles

	t: Turtle
	n: number of isosceles triangles in the final polygon
	radius:  radius of the final polygon
	"""
	angle = 360.0 / n
	peak_angle = angle / 2
	for i in range(n):
		isosceles(t, peak_angle, radius)
		t.lt(angle)


def draw_pie(t, n, radius):
	"""Draws a pie, then moves to the right side

	t: Turtle
	n: number of isosceles triangles in the final polygon
	radius:  radius of the final polygon
	"""
	polygon_triangle(t, n, radius)
	t.pu()
	t.fd(radius*2)
	t.pd()




if __name__ == '__main__':
	bob = turtle.Turtle()
	
	#isosceles(bob, 60/2, 50)
	#polygon_triangle(bob, 5, 50)
	bob.pu()
	bob.bk(180)
	bob.pd()
	bob.delay = 0.008
	# draw polypies with different number of sides
	twist = 50
	draw_pie(bob, 5, twist)
	draw_pie(bob, 6, twist)
	draw_pie(bob, 7, twist)

	turtle.mainloop()