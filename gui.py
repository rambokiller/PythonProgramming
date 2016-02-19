#!/usr/bin/env python3
#Now this is what I'm talking about
from graphics import *
win = GraphWin('myEye')

leftEye = Circle(Point(80,50),10)
leftEye.setFill('yellow')
leftEye.setOutline('red')
leftEye.draw(win)

rightEye = leftEye.clone()
rightEye.draw(win)
rightEye.move(30,0)
myI=input()

