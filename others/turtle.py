# square.py
import turtle

def square(n):  
  for i in range(4):
    turtle.forward(n)
    turtle.right(90)

square(30)
turtle._root.mainloop()