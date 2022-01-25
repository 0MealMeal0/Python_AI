import turtle
t = turtle.Turtle()
t.shape("turtle")

t.penup()
t.goto(100, 100)
t.write("거북이가 여기로 오면 양수")

t.goto(100, 0)
t.write("거북이가 여기로 오면 0")

t.goto(100, -100)
t.write("거북이가 여기로 오면 음수")

t.goto(0, 0)
t.pendown()

s = turtle.textinput("", "숫자를 입력하세요.: ")
n = int(s)

if n > 0:
    t.goto(100, 100)

if n == 0:
    t.goto(100, 0)

if n < 0:
    t.goto(100, -100)

turtle.done()