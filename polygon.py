import turtle
import math

def	polyline(t, n, length, angle):
	for i in range(n):
		t.fd(length)
		t.rt(angle)

def polygon(t, n, length):
	angle = 360 / n
	polyline(t, n, length, angle)

def arc(t, r, angle):
	arc_length = 2 * math.pi * r * angle / 360
	n = int(arc_length / 3) + 1
	step_length = arc_length / n
	step_angle = angle / n
	polyline(t, n, step_length, step_angle)

def circle(t, r):
	arc(t, r, 360)

def star(t, length):
	polyline(t, 5, length, 144)



if __name__ == "__main__":
	bob = turtle.Turtle()
	circle(bob, 100)
	polygon(bob, 6, 100)
	star(bob, 100)
	arc(bob, 100, 90)
	turtle.mainloop()
