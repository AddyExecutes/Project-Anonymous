# Importing basics
import pygame
import eventlistener

import rgbcode
import workspace
import taskbar
import newproject

# Initializing the lib
pygame.init()

# Display & Title defining
default_W = 1600
default_H = 900
default_WH = (default_W, default_H)

app_name = "Project Anonymous"
title = app_name
def change_title(new_title: str): global title ; title = new_title


# Display setup
screen = pygame.display.set_mode(default_WH, pygame.RESIZABLE)

# Screen API (for external usage)
scr_W, scr_H = screen.get_width(), screen.get_height()

# Vars
running = True

# Child Vars
permission_workspace = True
permission_taskbar = True
permission_newproject = True



# Parent function
def batman():

    # Priority - bottommost
    if permission_workspace: workspace.workspace()

    # Priority - over other windows
    if permission_newproject: newproject.window()

    # Priority - topmost
    if permission_taskbar: taskbar.taskbar()

# Event Loop
while running:

    # Title setup
    pygame.display.set_caption(title)

    # Event loop
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False


    # Default BG
    screen.fill(rgbcode.theme)
        
    # Calling the parent function
    batman()

    pygame.display.update()

pygame.quit()