#############################################################################################
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\ Homework 5//////////////////////////////////////////////#
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\ Anush Mattapalli///////////////////////////////////////////#
#\\\I worked on the homework assignment alone, using only this semester's course materials//#
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\amattapalli3@gatech.edu////////////////////////////////////////#
#############################################################################################

from Graphics import *
from Myro import *

init("COM4")

# I'm Free of these restraining programs :D
# For perfect use of this program, push the direction you would like to go only once
f = open("robotMovements.txt","w")
def handleKeyPress(win, event):
    x = getKeyPressed()
    print(x)
    if (x == "Up"):
        forward(1,.1)
        f.write("forward .1")
        f.write(get("light",0,"\n"))
    elif (x == "Down"):
        backward(1,.1)
        f.write("backward .1")
        f.write(get("light",0,"\n"))
    elif (x == "Right"):
        turnRight(1,.1)
        f.write("turnRight .1")
        f.write(get("light",0,"\n"))
    elif (x == "Left"):
        turnLeft(1,.1)
        f.write("turnLeft .1")
        f.write(get("light",0,"\n"))
    elif (x == "space"):
        stop()
    elif (x == "b"):
        beep(.5,1500)
    else:
        print("Try The Arrow Keys")

def handleKeyRelease(win, event):
    x = getKeyPressed()
    if (x == "Right"):
        stop()
        print("stopped")
    elif (x == "Left"):
        stop()
        print("stopped")

win = Window()
onKeyPress(handleKeyPress)
onKeyRelease(handleKeyRelease)


