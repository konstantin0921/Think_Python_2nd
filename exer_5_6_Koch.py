import turtle

def koch(t, length):
    if length < 10:
        t.fd(length)
        return
    koch(t, length/3)
    angle = 60
    t.lt(angle)
    koch(t, length/3)
    t.rt(2*angle)
    koch(t, length/3)
    t.lt(angle)
    koch(t, length/3)

def snowflake(t, n):
    """Draws a snowflake (a triangle with a Koch curve for each side)."""
    for i in range(3):
        koch(t, n)
        t.rt(120)

if __name__ == '__main__':
    bob = turtle.Turtle()
    #koch(bob, 120)

    bob.pu()
    bob.goto(-150, 90)
    bob.pd()
    snowflake(bob, 300)
    turtle.mainloop()