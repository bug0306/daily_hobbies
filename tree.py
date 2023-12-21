import turtle
import random as r
def draw_treec():
	pen=turtle.Turtle()
	n = 100.0
	pen.speed(1000)  
	pen.pensize(5)  
	pen.goto(0,40)
	pen.left(90)
	pen.forward(250)             
	pen.color("orange", "yellow") 
	pen.begin_fill()
	pen.left(126)

	for i in range(5): 
		pen.forward(n / 5)
		pen.right(144) 
		pen.forward(n / 5)
		pen.left(72) 
	pen.end_fill()
	pen.right(126)


	def drawlight():
		if r.randint(0, 50) == 0: 
			pen.color('tomato')
			pen.circle(3) 
		elif r.randint(0, 30) == 1:
			pen.color('orange')  
			pen.circle(4) 
		elif r.randint(0, 50) == 2:
			pen.color('blue')  
			pen.circle(2)  
		elif r.randint(0, 30) == 3:
			pen.color('white')  
			pen.circle(4) 
		else:
			pen.color('dark green') 


	pen.color("dark green") 
	pen.backward(n * 4.8)


	def tree(d, s): 
		if d <= 0: return
		pen.forward(s)
		tree(d - 1, s * .8)
		pen.right(120)
		tree(d - 3, s * .5)
		drawlight() 
		pen.right(120)
		tree(d - 3, s * .5)
		pen.right(120)
		pen.backward(s)

	pen.speed(2000)
	tree(15, 100)
	pen.speed(1000)
	pen.backward(50)

	for i in range(100): 
		a = 200 - 400 * r.random()
		b = 10 - 20 * r.random()
		pen.up()
		pen.forward(b)
		pen.left(90)
		pen.forward(a)
		pen.down()
		if r.randint(0, 1) == 0:
			pen.color('tomato')
		else:
			pen.color('wheat')
		pen.circle(2)
		pen.up()
		pen.backward(a)
		pen.right(90)
		pen.backward(b)

	def drawsnowman(n,m,a,b):  # 画雪人 (n,m)是头和身子交点的坐标，a是头的大小，m是身体的大小
		turtle.goto(n, m)
		turtle.pencolor("white")
		turtle.pensize(2)
		turtle.fillcolor("white")
		turtle.seth(0)
		turtle.begin_fill()
		turtle.circle(a)
		turtle.end_fill()
		turtle.seth(180)
		turtle.begin_fill()
		turtle.circle(b)
		turtle.end_fill()
		turtle.pencolor("black")
		turtle.fillcolor("black")
		turtle.penup()    # 右眼睛
		turtle.goto(n-a/4, m+a)
		turtle.seth(0)
		turtle.pendown()
		turtle.begin_fill()
		turtle.circle(2)
		turtle.end_fill()
		turtle.penup()    # 左眼睛
		turtle.goto(n+a/4, m+a)
		turtle.seth(0)
		turtle.pendown()
		turtle.begin_fill()
		turtle.circle(2)
		turtle.end_fill()
		turtle.penup()  # 画嘴巴
		turtle.goto(n, m+a/2)
		turtle.seth(0)
		turtle.pendown()
		turtle.fd(5)
		turtle.penup()       # 画扣子
		turtle.pencolor("red")
		turtle.fillcolor("red")
		turtle.goto(n, m-b/4)
		turtle.pendown()
		turtle.begin_fill()
		turtle.circle(2)
		turtle.end_fill()
		turtle.penup()
		turtle.pencolor("yellow")
		turtle.fillcolor("yellow")
		turtle.goto(n, m-b/2)
		turtle.pendown()
		turtle.begin_fill()
		turtle.circle(2)
		turtle.end_fill()
		turtle.penup()
		turtle.pencolor("orange")
		turtle.fillcolor("orange")
		turtle.goto(n, m-(3*b)/4)
		turtle.pendown()
		turtle.begin_fill()
		turtle.circle(2)
		turtle.end_fill()

	drawsnowman(-240, -200, 20, 30)
	drawsnowman(-290, -200, 30, 40)

	def drawsnow(): 
		turtle.ht() 
		turtle.pensize(2)  
		turtle.speed(1000)
		for i in range(200): 
			turtle.pencolor("white") 
			turtle.pu() 
			turtle.setx(r.randint(-(turtle.window_width()//2),turtle.window_width()//2)) 
			turtle.sety(r.randint(-120, 250)) 
			turtle.pd()
			dens = 6  
			snowsize = r.randint(1, 10)  
			for j in range(dens):  
				# turtle.forward(int(snowsize)) 
				turtle.fd(int(snowsize))
				turtle.backward(int(snowsize))
				# turtle.bd(int(snowsize)) 
				turtle.right(int(360 / dens)) 
	drawsnow() 
dx = 650
def draw_tree():
	circle = turtle.Turtle()
	circle.shape('circle')
	circle.color('red')
	circle.speed(0)
	circle.up()

	square = turtle.Turtle()
	square.shape('square')
	square.color('green')
	square.speed(0)
	square.up()

	k = 0
	for i in range(1,17):
		y = 30 * i
		for j in range(i-k):
			x = 30 * j
			square.goto(x-dx, 280 - y)
			square.stamp()
			square.goto(-x-dx, 280 - y)
			square.stamp()

		if i % 4 == 0:
			x = 30 * (j+1)
			circle.color('red')
			circle.goto(-x-dx,-y+280)
			circle.stamp()
			circle.goto(x-dx,-y+280)
			circle.stamp()
			k += 2

		if i % 4 == 3:
			x = 30 * (j+1)
			circle.color('yellow')
			circle.goto(-x-dx,-y+280)
			circle.stamp()
			circle.goto(x-dx,-y+280)
			circle.stamp()

	square.color('brown')
	for i in range(17,20):
		y = 30 * i
		for j in range(3):
			x = 30 * j
			square.goto(x-dx,-y+280)
			square.stamp()
			square.goto(-x-dx,-y+280)
			square.stamp()

def draw_star(t, color):
	t.color(color)
	t.begin_fill()
	for k in range(5):
		t.forward(13)
		t.right(144)
		t.forward(13)
	t.end_fill()
def show_lirics(turtlepen,line):
	turtlepen.color("yellow")
	turtlepen.penup()
	turtlepen.hideturtle()
	turtlepen.goto(0, -470)
	turtlepen.clear() 
	turtlepen.write(line, align="center", font=("楷体", 32, "normal"))
def show_lirics1(turtlepen,line):
	turtlepen.color("yellow")
	turtlepen.penup()
	turtlepen.hideturtle()
	turtlepen.goto(0, -450)
	turtlepen.write(line, align="center", font=("楷体", 42, "normal"))
	turtle.done()
