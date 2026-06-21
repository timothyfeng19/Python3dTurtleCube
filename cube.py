import turtle
import math

screen = turtle.Screen()
screen.title("3D Cube with Perspective Projection")
screen.setup(width=800, height=800)
screen.tracer(0)

cube = turtle.Turtle()
cube.hideturtle()
cube.penup()

rotation_x = 0
rotation_y = 0
up = 0
down = 0
left = 0
right = 0
forward = 0
mleft = 0
backward = 0
mright = 0
mup = 0
mdown = 0
zoom = 800
rotation_speed = 0.01
move_speed = 0.01
cube_x = 0
cube_y = 0
cube_z = 5

def coords(x, y, z):
    global zoom, rotation_x, rotation_y, cube_x, cube_y, cube_z

    temp_x = x * math.cos(rotation_y) + (y * math.sin(rotation_x) + z * math.cos(rotation_x)) * math.sin(rotation_y)
    temp_y = y * math.cos(rotation_x) - z * math.sin(rotation_x)
    temp_z = -x * math.sin(rotation_y) + (y * math.sin(rotation_x) + z * math.cos(rotation_x)) * math.cos(rotation_y)
    
    factor = zoom / (-temp_z + cube_z)

    return (temp_x + cube_x) * factor, (temp_y + cube_y) * factor

def draw(list, color):
    global cube

    cube.penup()
    cube.goto(list[0])
    cube.pencolor(color)
    cube.pendown()

    for i in range(len(list)):
        cube.goto(list[i])

    cube.goto(list[0])
    cube.penup()

def write(text, x, y, color, center, info):
    global cube

    cube.penup()
    cube.goto(x, y)
    cube.pencolor(color)
    cube.pendown()
    cube.write(text, False, align = center, font = info)
    cube.penup()

def rotate_up():
    global up
    up = 1

def rotate_down():
    global down
    down = 1

def rotate_left():
    global left
    left = 1

def rotate_right():
    global right
    right = 1

def move_forward():
    global forward
    forward =  1

def move_left():
    global mleft
    mleft =  1

def move_backward():
    global backward
    backward =  1

def move_right():
    global mright
    mright =  1

def move_up():
    global mup
    mup =  1

def move_down():
    global mdown
    mdown =  1

def release_up():
    global up
    up = 0

def release_down():
    global down
    down = 0

def release_left():
    global left
    left = 0

def release_right():
    global right
    right = 0

def release_forward():
    global forward
    forward =  0

def release_mleft():
    global mleft
    mleft =  0

def release_backward():
    global backward
    backward =  0

def release_mright():
    global mright
    mright =  0

def release_mup():
    global mup
    mup =  0

def release_mdown():
    global mdown
    mdown =  0

screen.onkeypress(rotate_up, "Up")
screen.onkeypress(rotate_down, "Down")
screen.onkeypress(rotate_left, "Left")
screen.onkeypress(rotate_right, "Right")
screen.onkeypress(move_forward, "w")
screen.onkeypress(move_left, "a")
screen.onkeypress(move_backward, "s")
screen.onkeypress(move_right, "d")
screen.onkeypress(move_up, "q")
screen.onkeypress(move_down, "e")

screen.onkeyrelease(release_up, "Up")
screen.onkeyrelease(release_down, "Down")
screen.onkeyrelease(release_left, "Left")
screen.onkeyrelease(release_right, "Right")
screen.onkeyrelease(release_forward, "w")
screen.onkeyrelease(release_mleft, "a")
screen.onkeyrelease(release_backward, "s")
screen.onkeyrelease(release_mright, "d")
screen.onkeyrelease(release_mup, "q")
screen.onkeyrelease(release_mdown, "e")

while True:
    cube.clear()

    front_face = [coords(1, 1, 1), coords(1, -1, 1), coords(-1, -1, 1), coords(-1, 1, 1)]
    back_face = [coords(1, 1, -1), coords(1, -1, -1), coords(-1, -1, -1), coords(-1, 1, -1)]
    top_face = [coords(1, 1, 1), coords(1, 1, -1), coords(-1, 1, -1), coords(-1, 1, 1)]
    bottom_face = [coords(1, -1, 1), coords(1, -1, -1), coords(-1, -1, -1), coords(-1, -1, 1)]

    guide = [coords(0, 0, 1), coords(0, 0, 2)]
    
    draw(front_face, "black")
    draw(back_face, "black")
    draw(top_face, "black")
    draw(bottom_face, "black")

    draw(guide, "red")

    write("Controls:", -380, -290, "black", 'left', ('Verdana', 15, 'normal'))
    write("← → : rotate left and right", -380, -310, "black", 'left', ('Verdana', 15, 'normal'))
    write("↑ ↓ : rotate up and down (along the red line)", -380, -330, "black", 'left', ('Verdana', 15, 'normal'))
    write("W A S D : move the cube around", -380, -350, "black", 'left', ('Verdana', 15, 'normal'))
    write("Q E : move the cube up and down", -380, -370, "black", 'left', ('Verdana', 15, 'normal'))

    rotation_x -= (up - down) * rotation_speed
    rotation_y -= (left - right) * rotation_speed

    cube_x += (mright - mleft) * move_speed
    cube_y += (mup - mdown) * move_speed
    cube_z += (forward - backward) * move_speed

    if cube_z <= 2:
        cube_z = 2 + move_speed

    screen.update()
    screen.listen()
