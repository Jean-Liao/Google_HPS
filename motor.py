from bluedot import BlueDot
from gpiozero import Robot
from signal import pause

bd = BlueDot()
robot = Robot(left=(9, 10), right=(7, 8))

def move(pos):
    if pos.top:
        robot.forward(pos.distance)
        print("f")
    elif pos.bottom:
        robot.backward(pos.distance)
        print("b")
    elif pos.left:
        robot.left(pos.distance)
        print("l")
    elif pos.right:
        robot.right(pos.distance)
        print("r")

def stop():
    robot.stop()

bd.when_pressed = move
bd.when_moved = move
bd.when_released = stop

pause()