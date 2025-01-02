import graphics
import rgbcode

taskbar_X = 0
taskbar_Y = 0
taskbar_H = 25

# Taskbar
def taskbar():

    from main import screen

    graphics.Shape.rect(rgbcode.taskbar, (taskbar_X, taskbar_Y, screen.get_width(), taskbar_H))