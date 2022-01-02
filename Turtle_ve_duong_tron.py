import turtle as t
t.shape("turtle")
t.goto(10-100,10) # tâm đường tròn I(10,10), bán kính 100
t.pensize(5)
t.color("green","red")# the same: t.pencolor("red"),t.fillcolor("green")
t.begin_fill()
t.circle(100)
t.end_fill()
t.done()