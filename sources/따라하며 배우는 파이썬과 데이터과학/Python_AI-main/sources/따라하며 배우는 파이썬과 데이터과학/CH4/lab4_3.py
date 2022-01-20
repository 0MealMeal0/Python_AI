import turtle
t = turtle.Turtle()
t.shape("turtle")


t.shapesize(3, 3)

while 1:
    order = str(input("명령을 입력하세요.: "))

    if(order == 'l'):
        t.left(90)
        t.forward(100)
    
    elif(order == 'r'):
        t.right(90)
        t.forward(100)
    
    elif(order == 'q'):
        exit()
    
    t.pendown()