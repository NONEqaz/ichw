import math
import turtle
wn = turtle.Screen()
def planetorbit (a, b, c, d, e, f):
    a.penup(),b.penup(),c.penup(),d.penup(),e.penup(),f.penup()
    a.shape("circle"),b.shape("circle"),c.shape("circle")
    d.shape("circle"),e.shape("circle"),f.shape("circle")
    t=0
    x1 = 1.1*math.cos(t)
    x2 = 1.5*math.cos(t)-0.2
    x3 = 2.3*math.cos(t)+0.7
    x4 = 3.0*math.cos(t)-0.9
    x5 = 3.5*math.cos(t)
    x6 = 3.65*math.cos(t)
    y1 = 1*math.sin(t)
    y2 = 1.3*math.sin(t)
    y3 = 1.6*math.sin(t)
    y4 = 2.8*math.sin(t)
    y5 = 1.25*math.sin(t)
    y6 = 2.4*math.sin(t)   
    scaledX1 = x1 * 100
    scaledX2 = x2 * 100
    scaledX3 = x3 * 100
    scaledX4 = x4 * 100
    scaledX5 = x5 * 100
    scaledX6 = x6 * 100
    scaledY1 = y1 * 100
    scaledY2 = y2 * 100
    scaledY3 = y3 * 100
    scaledY4 = y4 * 100
    scaledY5 = y5 * 100
    scaledY6 = y6 * 100
    a.goto (scaledX1, scaledY1), b.goto (scaledX2, scaledY2)
    c.goto (scaledX3, scaledY3), d.goto (scaledX4, scaledY4)
    e.goto (scaledX5, scaledY5), f.goto (scaledX6, scaledY6)
    a.pendown(),b.pendown(),c.pendown(),d.pendown(),e.pendown(),f.pendown()
    while 1:
        t = t + 0.01
        x1 = 1.1*math.cos(t)
        x2 = 1.5*math.cos(t)-0.2
        x3 = 2.3*math.cos(t)+0.7
        x4 = 3.0*math.cos(t)-0.9
        x5 = 3.5*math.cos(t)
        x6 = 3.65*math.cos(t)
        y1 = 1*math.sin(t)
        y2 = 1.3*math.sin(t)
        y3 = 1.6*math.sin(t)
        y4 = 2.8*math.sin(t)
        y5 = 1.25*math.sin(t)
        y6 = 2.4*math.sin(t) 
        scaledX1 = x1 * 100
        scaledX2 = x2 * 100
        scaledX3 = x3 * 100
        scaledX4 = x4 * 100
        scaledX5 = x5 * 100
        scaledX6 = x6 * 100
        scaledY1 = y1 * 100
        scaledY2 = y2 * 100
        scaledY3 = y3 * 100
        scaledY4 = y4 * 100
        scaledY5 = y5 * 100
        scaledY6 = y6 * 100
        a.goto (scaledX1, scaledY1), b.goto (scaledX2, scaledY2)
        c.goto (scaledX3, scaledY3), d.goto (scaledX4, scaledY4)
        e.goto (scaledX5, scaledY5), f.goto (scaledX6, scaledY6)
    a.penup(),b.penup(),c.penup(),d.penup(),e.penup(),f.penup()
def  main():
    turtle.title ('Planets')
    turtle.setup (1280, 760, 0, 0)
    Sun = turtle.Turtle()
    Sun.color("yellow")
    Sun.shape("circle")
    Mercury = turtle.Turtle()
    Mercury.color("Blue")
    Venus=turtle.Turtle()
    Venus.color("green")
    Earth=turtle.Turtle()
    Earth.color("black")
    Mars=turtle.Turtle()
    Mars.color("red")
    Jupiter=turtle.Turtle()
    Jupiter.color("brown")
    Saturn=turtle.Turtle()
    Saturn.color("skyblue")
    planetorbit(Mercury,Venus,Earth,Mars,Jupiter,Saturn)
if __name__ == "__main__":
    main()