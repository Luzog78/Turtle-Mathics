from turtle import speed, pu, pd, goto, circle as c, dot, write, \
                   hideturtle, exitonclick, tracer, update, setup
from math import pi, cos, sin

setup(width=1.0, height=1.0, startx=0, starty=0)
speed(0)


def circle(radius: int):
  pu()
  goto(0, -radius)
  pd()
  
  c(radius)

  pu()
  goto(0, 0)
  pd()


def dot_at(i: float, modulo: int, radius: int):
  return (sin(i * 2 * pi / modulo) * radius,
          cos(i * 2 * pi / modulo) * radius)


def dots(modulo: int, radius: int, labels: bool = False):
  for i in range(modulo):
    pu()
    goto(dot_at(i, modulo, radius))
    dot(4)
    goto(dot_at(i, modulo, radius + (28 if i > modulo / 4 and i < 3 * modulo / 4 else 18)))
    write(f"{i}", align="center" if i == 0 or i == modulo / 2 else "left" if i < modulo / 2 else "right", font=("Verdana", 10, "normal"))
    pd()
  pu()
  goto(0, 0)
  pd()


def links(table: float, modulo: int, radius: int):
  for i in range(1, modulo):
    pu()
    goto(dot_at(i, modulo, radius))
    pd()
    goto(dot_at(i * table, modulo, radius))
  pu()
  goto(0, 0)
  pd()


table, modulo, radius = 2, 100, 300  # 37.6, 500, 300
instant = False

if instant:
  tracer(0, 0)
circle(radius)
dots(modulo, radius, True)
links(table, modulo, radius)
hideturtle()
if instant:
  update()
exitonclick()
