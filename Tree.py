import turtle
import random
import math

def reset(numC):
    while numC>255:
        numC -= 255
    return numC
        

def tree(length,t,color):
    if length>=5:
        newColor = (reset(color[0]+20*math.sin(random.random()*math.pi)),reset(color[1]+20*math.sin(random.random()*math.pi)),reset(color[2]+20*math.sin(random.random()*math.pi)))
        
        t.color(newColor)
        
        #Generate 2 angles
        angle1 = 1+10*math.sin(random.random()*math.pi)
        angle2 = 1+10*math.sin(random.random()*math.pi)
        
        length += 5*math.sin(random.random()*2*math.pi)
        
        t.width((length+15)//15)
        t.pendown()
        
        t.forward(length)
        
        #Draw branch 1
        t.right(angle1)
        tree(length-(5+10*math.sin(random.random()*math.pi)),t,newColor)
        
        #Draw branch 2
        t.left(angle1+angle2)
        tree(length-(5+10*math.sin(random.random()*math.pi)),t,newColor)
        
        #Head back
        t.right(angle2)
        t.penup()
        t.backward(length)
t = turtle.Turtle()

t.color("black")
t.left(90)
t.speed(0)
t.penup()
t.setpos(0,-1000)
t.pendown()
tree(150,t,(0,0,0))