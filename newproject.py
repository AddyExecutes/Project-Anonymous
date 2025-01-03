import rgbcode
import graphics
import eventlistener

window_active = True
window_float = False

win_X = 50
win_X_diff = 0

win_Y = 50
win_Y_diff = 0
cursor_default = False


# Project name
project_name = "Project 1"

def window():

    global window_active, window_float, win_X, win_X_diff, win_Y, win_Y_diff
    global cursor_default

    import main


    win_W = 700
    win_H = 500

    coordinates = (win_X, win_Y, win_W, win_H)
    bdr_rad = 3
    heading = "New Project"
    header_H = 30

    # Mouse coordinates
    mx, my = eventlistener.Event.mouse_pos()
            



    # Window
    graphics.Shape.rect(rgbcode.sub_window, coordinates, True, borderRadius = bdr_rad)
    
    """ Header and Heading """
    if window_active:
        graphics.Shape.rect(rgbcode.header_active, (coordinates[0], coordinates[1], coordinates[2], header_H), borderRadius = bdr_rad)
        graphics.Text.text(heading, (coordinates[0]+10, coordinates[1]+7), textFG = rgbcode.light_font)

    else:
        graphics.Shape.rect(rgbcode.header_inactive, (coordinates[0], coordinates[1], coordinates[2], header_H), borderRadius = bdr_rad)
        graphics.Text.text(heading, (coordinates[0]+10, coordinates[1]+7), textFG = rgbcode.light_font_secondary)



    # Floating mechanism
    if eventlistener.Event.hovers(win_X, win_Y, win_W, header_H):

        if eventlistener.Event.get_event() == "leftclickdown":
            win_X_diff = mx - win_X
            win_Y_diff = my - win_Y
            window_float = True

        elif eventlistener.Event.get_event() == "leftclickup":
            win_X_diff = 0
            win_Y_diff = 0
            window_float = False

    if window_float:
        win_X = mx - win_X_diff
        win_Y = my - win_Y_diff



    # Window activation and deactivation
    if eventlistener.Event.get_event() == "leftclickdown":
        if eventlistener.Event.hovers(win_X, win_Y, win_W, win_H): window_active = True
        else: window_active = False



    """ Body """

    # Name of the project

    # Name entry
    name_entry_padding = 20
    name_entry_X = coordinates[0] + name_entry_padding
    name_entry_Y = coordinates[1] + 50
    name_entry_W = coordinates[2] - (name_entry_padding*2)
    name_entry_H = 20

    graphics.Shape.rect(rgbcode.entry_BG, (name_entry_X, name_entry_Y, name_entry_W, name_entry_H))
    

    # Name
    graphics.Text.text(project_name, (name_entry_X+5, name_entry_Y+2), textFG = rgbcode.dark_font)















    # List of widgets
    widgets = [
        {"x": name_entry_X, "y": name_entry_Y, "w": name_entry_W, "h": name_entry_H, "cursor": "i-beam"}
    ]


    # Check if mouse is hovering over any widget
    for widget in widgets:

        if eventlistener.Event.hovers(widget["x"], widget["y"], widget["w"], widget["h"]):
            main.cursortype = widget["cursor"]
            cursor_default = False
            break
        else:
            cursor_default = True

    # Set default cursor if no widget is hovered
    if cursor_default:
        main.cursortype = "arrow"









