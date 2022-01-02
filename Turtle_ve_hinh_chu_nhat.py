import turtle as t
a = 100 # a là chiều dài
b = 50 # b là chiều rộng
t.pensize(3)
t.color("red","blue")
t.begin_fill()
t.forward(a)
t.right(90)
t.forward(b)
t.right(90)
t.forward(a)
t.right(90)
t.forward(b)
t.right(90)
t.end_fill()
t.done()