import turtle
import random
import math

#creating window
wn=turtle.Screen()
wn.title("Pac-Man by Ishaan")
wn.bgcolor("white")
wn.tracer(0)   

#creating boundaries
b=turtle.Turtle()
b.color("Black")
b.penup()
b.setposition(-300, -300)
b.pendown()
b.pensize(5)
for i in range(4):
    b.forward(600)
    b.left(90)
b.hideturtle()

#creating pac man
pm=turtle.Turtle()
pm.color("gold")
pm.shape("circle")
pm.penup()
pm.speed(0)

#creating score turtle
p=turtle.Turtle()
score=0

#making goals
mg=5
gls=[]
for i in range(mg):
    gls.append(turtle.Turtle())
    gls[i].color("Blue4")
    gls[i].shape("triangle")
    gls[i].penup()
    gls[i].speed(0)
    gls[i].setposition(random.randint(-295,295),random.randint(-295,295))
    gls[i].right(random.randint(0,360))

#making traps
ts=[]
for i in range(mg):
    ts.append(turtle.Turtle())
    ts[i].color("maroon")
    ts[i].shape("square")
    ts[i].penup()
    ts[i].speed(0)
    ts[i].setposition(random.randint(-295,295),random.randint(-295,295))
    ts[i].left(random.randint(0,360))

#setting speed
speed = 2
def travel():
    pm.forward(speed)
    wn.ontimer(travel, 10)
#taking  direction input
wn.onkey(lambda: pm.setheading(90), 'Up')
wn.onkey(lambda: pm.setheading(180), 'Left')
wn.onkey(lambda: pm.setheading(0), 'Right')
wn.onkey(lambda: pm.setheading(270), 'Down')
wn.listen()

travel()

#creating empty list
ds=[]

#main loop
while True:
    wn.update()
    #boundary deflection
    if pm.xcor()>300 or pm.xcor()<-300:
        pm.left(180)
    if pm.ycor()>300 or pm.ycor()<-300:
        pm.left(180)
    #move the goal
    for i in gls:
        i.forward(2)
        #boundarychecking
        if i.xcor()>295 or i.xcor()<-295:
            i.right(random.randint(120,180))
        if i.ycor()>295 or i.ycor()<-295:
            i.right(random.randint(120,180))
        #collision checking
        if pm.distance(i)<15:
            ds.append(i)
            i.hideturtle()
            i.penup()
            i.setposition(-303,-303)
            score+=1
    #moving the traps
    for i in ts:
        i.forward(2)
        #boundarychecking
        if i.xcor()>295 or i.xcor()<-295:
            i.right(random.randint(120,180))
        if i.ycor()>295 or i.ycor()<-295:
            i.right(random.randint(120,180))
        #collision checking
        if pm.distance(i)<15:
            ds.append(i)
            i.hideturtle()
            i.penup()
            i.setposition(-303,-303)
            score-=1
    p.undo()
    p.penup()
    p.setposition(280,305)
    p.color("yellow2")
    p.pendown()
    m='Score:'+str(score)
    p.write(m,False,align="left",font=("Arial",15,"normal"))
    if len(ds)>=5:
        wn.clear()
        wn.bgcolor("white")
        #give game over and score
        b.penup()
        b.hideturtle()
        b.setposition(0,150)
        b.color("maroon")
        estring="Score:"+(str(score))
        b.write("Game Over",False,align="center",font=("Comic Sans MS",40,"bold"))
        b.setposition(0,-150)
        b.write(estring,False,align="center",font=("Comic Sans MS",30,"bold"))

wn.mainloop()
