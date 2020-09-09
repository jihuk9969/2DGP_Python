import turtle as t

size = 100
startX = 0
startY = 0
endX = 500
endY = 500

def move(x,y):
    t.penup()
    t.goto(x,y)
sssssd
disX = 0
if startX > endX:
    disX = startX-endX
else:
    disX = endX-startX

x = disX // size

disY = 0
if startY > endY:
    disY = startY-endY
else:
    disY = endY-startY

y = disY // size

move(startX,startY)

print(x)
for i in range(x):
    move(i*size,startY)
    t.setheading(90)
    t.forward(disY)
    
for j in range(y):
    move(startX,j*size)
    t.setheading(0)
    t.forward(disX)
        
        
        
    
