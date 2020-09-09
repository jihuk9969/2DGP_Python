import turtle
turtle.shape("turtle")
turtle.speed(0)
turtle.pensize(3)

def move_pen(x,y):
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    
def korean_j(x,y,dis):
    move_pen(x,y)
    turtle.setheading(0)
    turtle.forward(dis)
    turtle.right(135)
    turtle.forward(dis*(2**0.5))
    turtle.right(-180)
    turtle.penup()
    turtle.forward((dis*(2**0.5))/2)
    turtle.right(90)
    turtle.pendown()
    turtle.forward((dis*(2**0.5))/2)

def korean_h(x,y,dis):
    move_pen(x,y)
    turtle.setheading(0)
    turtle.forward(dis)
    move_pen(x-dis/5,y-dis/5)
    turtle.forward(dis+dis*2/5)
    move_pen(x+dis/2,y-dis*2/5-dis)
    turtle.circle(dis/2)

def korean_k(x,y,dis):
    move_pen(x,y)
    turtle.setheading(0)
    turtle.forward(dis)
    turtle.right(90)
    turtle.forward(dis)

    
def korean_i(x,y,dis):
    move_pen(x,y)
    turtle.setheading(270)
    turtle.forward(dis)

def korean_yeo(x,y,dis):
    move_pen(x,y)
    turtle.setheading(270)
    turtle.forward(dis/3)
    turtle.right(90)
    turtle.forward(dis/3)
    turtle.penup()
    turtle.right(180)
    turtle.forward(dis/3)
    turtle.pendown()
    turtle.right(90)
    turtle.forward(dis/3)
    turtle.right(90)
    turtle.forward(dis/3)
    turtle.penup()
    turtle.right(180)
    turtle.forward(dis/3)
    turtle.pendown()
    turtle.right(90)
    turtle.forward(dis/3)
    




def korean(con,vow,sup,x,y,dis):
    if con =='j':
        korean_j(x-dis*2/3,y+(dis*2)/3,(dis*2)/3)
    elif con == 'h':
        korean_h(x-dis*2/3,y+(dis*2)/3,(dis*2)/3)

    if vow =='i':
        korean_i(x+dis/3,y+(dis*3/4),dis*3/4)
    elif vow == 'yeo':
        korean_yeo(x+dis/3,y+(dis*3/4),dis*3/4)

    if sup =='k':
        korean_k(x-dis/2,y-(dis*3/4),dis*3/4)
    


korean('j','i','',-100,50,100)

korean('h','yeo','k',50,50,100)

turtle.exitonclick()
