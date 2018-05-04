import turtle
from book4_3 import arc

def petal(t, r, angle):
	"""Draws a petal using two arcs

	t: a Turtle object

	r: radius of the arcs(圆弧)

	angle: angle (degrees) that subtends the arcs
	"""

	for i in range(2):
		arc(t, r, angle)
		t.lt(180-angle)

def flower(t, r, angle, n):
	"""Draws a flower with n petals

	t: Turtle object
	n: number of petals
	r: radius of the arcs
	angle: angle (degrees) that subtends the arcs
	"""
	for i in range(n):
		petal(t, r, angle)
		t.lt(360.0 / n)

def move(t, length):
    """Move Turtle (t) forward (length) units without leaving a trail.
    Leaves the pen down.
    """
    t.pu()
    t.fd(length)
    t.pd()

if __name__ == '__main__':
	bob = turtle.Turtle()
	bob.delay = 0.008
	
	# draw a sequence of three flowers, as shown in the book.
	move(bob, -100)
	flower(bob, 60.0, 60.0, 7)

	move(bob, 100)
	flower(bob, 40.0, 80.0, 10)

	move(bob, 100)
	flower(bob, 140.0, 20.0, 20)

	bob.hideturtle()

	turtle.mainloop()

