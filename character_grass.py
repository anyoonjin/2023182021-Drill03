from pico2d import *
import math

open_canvas()

grass=load_image('grass.png')
boy=load_image('character.png')

def draw_boy(x,y):
    clear_canvas_now()
    boy.draw_now(x,y)
    delay(0.1)

def run_circle():
    print('circle')
    
    r,cx,cy=300,800//2,600/2
    
    for degree in range(0,360,3):
        theta=math.radians(degree)
        x=r*math.cos(theta)+cx
        y=r*math.sin(theta)+cy
        draw_boy(x,y)
        
    pass

def run_top():
    print('top')
    for x in range(0,800,10):
        draw_boy(x,550)
    pass

def run_right():
    print('right')
    for y in range(550,0,-10):
        draw_boy(790,y)
    pass

def run_bottom():
    print('bottom')
    for x in range(800,0,-10):
        draw_boy(x,50)
    pass

def run_left():
    print('left')
    for y in range(0,550,10):
        draw_boy(10,y)
    pass
  
def run_rectangle():
    print('rectangle')
    run_top()
    run_right()
    run_bottom()
    run_left()
    
    pass

def run_t_bottom():
    print('t_bottom')
    for x in range(200,700,10):
        draw_boy(x,100)
    pass

def run_t_left():
    print('t_left')
    y=475
    for x in range(450,200,-10):
        y-=15
        draw_boy(x,y)
    pass

def run_t_right():
    print('t_right')
    y=100
    for x in range(700,450,-10):
        y+=15
        draw_boy(x,y)
    print(y)
    pass

def run_triangle():
    run_t_bottom()
    run_t_right()
    run_t_left()

    pass

while True:
    run_circle()
    run_rectangle()
    run_triangle()
    break

close_canvas()
