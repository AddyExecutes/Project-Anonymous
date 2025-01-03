# Importing basics
import pygame

import rgbcode
import workspace
import taskbar
import newproject

# Initializing the lib
pygame.init()

# Setting the clock
clock = pygame.time.Clock()

# Display & Title defining
default_W = 1600
default_H = 900
default_WH = (default_W, default_H)

app_name = "Project Anonymous"
title = app_name
FPS = 144

def change_title(new_title: str): global title ; title = new_title


# Display setup
screen = pygame.display.set_mode(default_WH, pygame.RESIZABLE)

# Screen API (for external usage)
scr_W, scr_H = screen.get_width(), screen.get_height()

# Vars
running = True
cursortype = "arrow" # This will be used to change the cursor type through the external files
desired_cursortype = ""

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


'''
Guide:

pygame.SYSTEM_CURSOR_ARROW       arrow
pygame.SYSTEM_CURSOR_IBEAM       i-beam
pygame.SYSTEM_CURSOR_WAIT        wait
pygame.SYSTEM_CURSOR_CROSSHAIR   crosshair
pygame.SYSTEM_CURSOR_WAITARROW   small wait cursor
                                (or wait if not available)
pygame.SYSTEM_CURSOR_SIZENWSE    double arrow pointing
                                northwest and southeast
pygame.SYSTEM_CURSOR_SIZENESW    double arrow pointing
                                northeast and southwest
pygame.SYSTEM_CURSOR_SIZEWE      double arrow pointing
                                west and east
pygame.SYSTEM_CURSOR_SIZENS      double arrow pointing
                                north and south
pygame.SYSTEM_CURSOR_SIZEALL     four pointed arrow pointing
                                north, south, east, and west
pygame.SYSTEM_CURSOR_NO          slashed circle or crossbones
pygame.SYSTEM_CURSOR_HAND        hand

'''

# Event Loop
while running:

    # Setting the FPS
    clock.tick(FPS)

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

    # Customizing the cursor

    if desired_cursortype != cursortype: # This statement does nothing but saves time and decreases load

        if cursortype == "arrow":
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
        elif cursortype == "i-beam":
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_IBEAM)
        elif cursortype == "wait":
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_WAIT)
        elif cursortype == "crosshair":
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_CROSSHAIR)
        elif cursortype == "waitarrow":
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_WAITARROW)
        elif cursortype == "sizenwse":
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_SIZENWSE)
        elif cursortype == "sizenesw":
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_SIZENESW)
        elif cursortype == "sizewe":
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_SIZEWE)
        elif cursortype == "sizens":
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_SIZENS)
        elif cursortype == "sizeall":
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_SIZEALL)
        elif cursortype == "no":
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_NO)
        elif cursortype == "hand":
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        
        desired_cursortype = cursortype

    # Updating the display
    pygame.display.update()

pygame.quit()