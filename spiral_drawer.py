import turtle
t = turtle.Pen()
turtle.bgcolor("black")
sides = input("how many sides? : ")
sides = eval(sides)
colors = ["red", "yellow", "blue", "green", "purple", "orange", "pink", "magenta", "brown", "white", "grey", "dark red",]
for x in range(1000):
    t.speed(x)
    t.pencolor(colors[x%sides])
    t.forward(x)
    t.left(360/sides+1)
    t.width(x/50)
