# shantanu urgunde (2403327)--5
# mukul chauhan (2403318)--5
# Vedansh paresh (2406341)--4
# chikkala bala (2404213)--4
# priya kumari (2403321)--4
# joshi nirav (2404219)--4

# this project is a mazerunner with it's core library being turtle
# you have to reach the end point within the given timelimit 

import turtle as t
import cv2
import random
import time
from threading import Thread


i = random.randint(0,1)

# Reading image
img_path = [r"C:\Users\Shantanu\Dropbox\PC\Pictures\college\mazefinal-ish.png",r"C:\Users\Shantanu\Dropbox\PC\Pictures\college\WhatsApp Image 2024-11-11 at 01.24.00_3f5ed078.png"]

img = cv2.imread(img_path[i])
if img is None:
    raise ValueError("Image not found")

# Convert the image to grayscale image
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Initialize the turtles
t1 = t.Turtle()
t2 = t.Turtle()
t3 = t.Turtle()
t2.hideturtle()
t.bgcolor("Black")
t1.shape("turtle")
t1.shapesize(1.5)
t1.speed(10)
t.screensize(700,600)

# Set the background image
t.bgpic(img_path[i])
t1.penup()

t3.penup() 
t3.goto(0, 260) 
t3.color("black") 
t3.hideturtle()

# Starting position
t1.goto(-250,50)

# Countdown timer in seconds
timer = 60 

#flag for gamewin
flag = True

# Check for wall
def check_for_wall(x, y):
    # Adjusting the coordinates based on the image dimensions and turtle screen size
    img_x = x + 350
    img_y = 300 - y
    
    return gray_img[img_y, img_x] < 200

def timer_func():
    global timer
    t3.hideturtle()

    while timer > 0 and flag:
        t3.clear()
        t3.penup()
        t3.goto(0, 260)
        t3.pendown()
        t3.color("black")
        t3.write(f"Time left: {timer} s", align="center", font=("Futura", 24, "normal"))
        time.sleep(1)
        timer -= 1
    check_lose()


def check_lose():
    if timer == 0:
        t3.clear()
        t1.hideturtle()
        t2.penup()
        t2.goto(-100, 210)
        t2.pendown()
        t2.color("Red")
        t2.write("You Lose", font=("Futura", 36, "normal"))
        t2.penup()


# Funtions for keybindings
def e():
    global flag
    
    t1.penup()
    t1.setheading(0)
    x = t1.position()
    
    # check conditions and do action
    if not check_for_wall(x[0] + 5, x[1]) and flag:
        t1.goto(x[0] + 5, x[1])
    
    if 250<=t1.xcor()<=310 and t1.ycor()>=190:
        t2.penup()
        t2.goto(-100,210)
        t2.pendown()
        t2.color("Red")
        t2.write("You Win", font=("Futura",36, "normal"))
        t2.penup()
        t3.penup()
        flag = False

    check_lose()    

def w():
    global flag
    
    t1.penup()
    t1.setheading(180)
    x = t1.position()

    # check conditions and do action
    if not check_for_wall(x[0] - 5, x[1]) and flag:
        t1.goto(x[0] - 5, x[1])
    
    if 250<=t1.xcor()<=310 and t1.ycor()>=190:
        t2.penup()
        t2.goto(-100,210)
        t2.pendown()
        t2.color("Red")
        t2.write("You Win", font=("Futura",36, "normal"))
        t2.penup()
        t3.penup()
        flag = False

    check_lose()    

def n():
    global flag
    
    t1.penup()
    t1.setheading(90)
    x = t1.position()

    # check conditions and do action
    if not check_for_wall(x[0], x[1] + 5) and flag:
        t1.goto(x[0], x[1] + 5)
    
    if 250<=t1.xcor()<=310 and t1.ycor()>=190:
        t2.penup()
        t2.goto(-100,210)
        t2.pendown()
        t2.color("Red")
        t2.write("You Win", font=("Futura",36, "normal"))
        t2.penup()
        t3.penup()
        flag = False    
    check_lose()

def s():
    global flag

    t1.penup()
    t1.setheading(270)
    x = t1.position()

    # check conditions and do action
    if not check_for_wall(x[0], x[1] - 5) and flag:
        t1.goto(x[0], x[1] - 5)
    
    if 250<=t1.xcor()<=310 and t1.ycor()>=190:
        t2.penup()
        t2.goto(-100,210)
        t2.pendown()
        t2.color("Red")
        t2.write("You Win", font=("Futura",36, "normal"))
        t2.penup()
        t3.penup()
        flag = False

    check_lose()

# Bind keys to functions
t.onkeypress(e, "d")
t.onkeypress(w, "a")
t.onkeypress(n, "w")
t.onkeypress(s, "s")


# Thing that does the job
t.listen()

# Start the timer
timer_thread = Thread(target= timer_func)
timer_thread.start()

t.mainloop()