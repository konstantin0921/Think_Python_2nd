import turtle

def draw(t, length, n):
    """Draws a symmetrical shape, which consists of multiple Polylines, 
    each polyline contains n pieces that are shorter and shorter(decreasing by 1*length)

    t: Turtle
    length: initial length
    n: the number of pieces in each polyline
    """
    if n == 0:
        return
    angle = 50
    t.fd(length*n)
    t.lt(angle)
    draw(t, length, n-1)
    t.rt(2*angle)
    draw(t, length, n-1)
    t.lt(angle)
    t.bk(length*n)


if __name__ == '__main__':
	bob = turtle.Turtle()
	draw(bob, 10, 5)

	turtle.mainloop()