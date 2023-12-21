import time
import playsound
import turtle
from turtle import *
from random import randint
from threading import Thread
from tree import draw_tree,draw_star,show_lirics,show_lirics1,draw_treec
import os
start_time = time.time()

def play_bg_music():
   playsound.playsound("system-files//cur_sonud.mp3")
def finish_music():
    playsound.playsound("system-files//finish-sound.mp3")
background_thread = Thread(target=play_bg_music)
background_thread.start()
time.sleep(1)

file_path = "text//wish.txt"
with open(file_path, 'r', encoding='utf-8') as file:
    content = file.readlines()
lyrics_lines = [line.strip(',') for line in content]

def create_rectangle(turtle, color, x, y, width, height):
    turtle.penup()
    turtle.color(color)
    turtle.fillcolor(color)
    turtle.goto(x, y)
    turtle.pendown()
    turtle.begin_fill()
    turtle.forward(width)
    turtle.left(90)
    turtle.forward(height)
    turtle.left(90)
    turtle.forward(width)
    turtle.left(90)
    turtle.forward(height)
    turtle.left(90)
    turtle.end_fill()
    turtle.setheading(0)

def create_circle(turtle, x, y, radius, color):
    turtle_pen.penup()
    turtle_pen.color(color)
    turtle_pen.fillcolor(color)
    turtle_pen.goto(x, y)
    turtle_pen.pendown()
    turtle_pen.begin_fill()
    turtle_pen.circle(radius)
    turtle_pen.end_fill()

BG_COLOR = "black"    #green:#2da716


turtle_pen = Turtle() 			  	
turtle_pen.speed(10) 			  	
# screen = turtle_pen.getscreen()  
screen=turtle.Screen() 	
screen.bgcolor(BG_COLOR)
screen.title("Merry Christmas")   	
screen.setup(width=1.0, height=1.0)	
screen.addshape('wishes//wish1.gif')
screen.addshape('santas//santa1.gif')
screen.addshape('bells//bell1.gif')

swidth=screen.window_width()
shigth=screen.window_height()

star1 = turtle.Turtle()
star1.speed(0)
star1.hideturtle()
star1.up()
star1.goto(-650, 290)
star1.down() 
draw_star(star1, 'red')
draw_tree()
draw_treec()
y = -100
tree_height = y + 340

create_circle(turtle_pen, 230, 300, 60, "yellow")
create_circle(turtle_pen, 200, 300, 60, BG_COLOR)

turtle_pen.speed(300)
number_of_stars = randint(50,60)
for _ in range(0,number_of_stars):
    x_star = randint(-(screen.window_width()//2),screen.window_width()//2)
    y_star = randint(tree_height+20, screen.window_height()//2)
    size = randint(5,20)
    turtle_pen.penup()
    turtle_pen.color('#FFEA00')
    turtle_pen.goto(x_star, y_star)
    turtle_pen.begin_fill()
    turtle_pen.pendown()
    for i in range(5):
        turtle_pen.forward(size)
        turtle_pen.right(144)
    turtle_pen.end_fill()

turtle_pen.speed(5)
turtle_pen.penup()
msg = "Wishing You A Very Merry Christmas ~ BoboDebuger"
turtle_pen.goto(0, -370) 
turtle_pen.color("orange")
turtle_pen.pendown()
turtle_pen.write(msg, move=False, align="center", font=("Arial", 25, "bold"))

win = turtle.Screen()
win.setup(width=1.0,height=1.0)
win.bgcolor('black')
win.title('Merry Christmas')
wishes = ['wishes/'+file for file in os.listdir('wishes/')]
santas = ['santas/'+file for file in os.listdir('santas/')]
bells = ['bells/'+file for file in os.listdir('bells/')]
for wish in wishes:
    win.addshape(wish)
for santa in santas:
    win.addshape(santa)
for bell in bells:
    win.addshape(bell)
star = turtle.Turtle()
star.speed(0)
star.hideturtle()
star.up()
star.goto(-650, 290)
star.down() 
w = turtle.Turtle()
w.speed(0)
w.up()
w.goto(530,-220)
s = turtle.Turtle()
s.speed(0)
s.up()
s.goto(530,220)
b = turtle.Turtle()
b.speed(0)
b.up()
b.goto(540,0)
windex = 1
sindex = 1
num = 0
colors = ['Yellow', 'Red', 'Gold', 'Orange']
turtlepen=turtle.Turtle()
line=0
while (time.time()-start_time)<380:
    c = colors[num % 4]
    draw_star(star, c)
    num += 1
    w.shape(f'wishes/wish{windex}.gif')
    s.shape(f'santas/santa{sindex}.gif')
    b.shape(f'bells/bell{windex}.gif')
    if windex+sindex==2:
        if line>=35:
           continue
        show_lirics(turtlepen,lyrics_lines[line])
        line=line+1
    windex = (windex + 1) % 4
    sindex = (sindex + 1) % 3
    if windex == 0:
        windex = 1
    if sindex == 0:
        sindex = 1
    if line>=35:
        if line>=35:
           turtlepen.clear()
        show_lirics1(turtlepen,lyrics_lines[line-1])
finish_music()
background_thread.join()
turtle_pen.hideturtle()
screen.mainloop()
