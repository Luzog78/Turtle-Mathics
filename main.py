from turtle import speed, pu, pd, goto, circle as c, dot, write, clear, \
                   hideturtle, exitonclick, tracer, update, setup
from math import pi, cos, sin
from time import sleep

setup(width=1.0, height=1.0, startx=0, starty=0)
hideturtle()
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


def draw_all(table: float, modulo: int, radius: int, instant: bool = False,
             _circle: bool = True, _dots: bool = True, _links: bool = True):
  """
  Intresting ones:  <br>
    -  3,      3    <br>
    -  3,     24    <br>
    -  2,     11    <br>
    - 11,    150    <br>
    - 13,     60    <br>
    - 13,    600    <br>
    - 37.6,  500    <br>
    - 45,     10    <br>
    - 45,    400    <br>
    - 45,    800    <br>
    - 45,   1200    <br>
  """
  if instant:
    tracer(0, 0)
  if _circle:
    circle(radius)
  if _dots:
    dots(modulo, radius, True)
  if _links:
    links(table, modulo, radius)
  if instant:
    update()


def demo():
  inp = input("Démo ? (1 / 2 / 3)  : ")
  if inp == "1":
    draw_all(45, 800, 350, True, _dots=False)
    
  elif inp == "2":
    for i in range(10_000):
      draw_all(i / 20, 10, 300, True)
      sleep(0.1)
      clear()
      
  elif inp == "3":
    for i in range(10_000):
      draw_all(i / 15 + 30, 600, 350, True, _circle=False, _dots=False)
      sleep(0.01)
      clear()

  else:
    demo()

demo()
exitonclick()
