import rgbcode
import graphics
import eventlistener

window_active = True
window_float = False

win_X = 50
win_X_diff = 0

win_Y = 50
win_Y_diff = 0

def window():

    global window_active, window_float, win_X, win_X_diff, win_Y, win_Y_diff


    win_W = 700
    win_H = 500

    coordinates = (win_X, win_Y, win_W, win_H)
    bdr_rad = 3
    heading = "New Project"
    header_H = 30

    # Mouse coordinates
    mx = eventlistener.Event.mouse_pos()[0]
    my = eventlistener.Event.mouse_pos()[1]

    # Floating mechanism
    if eventlistener.Event.hovers(win_X, win_Y, win_W, header_H, "hand"):

        if eventlistener.Event.get_event() is "leftclickdown":
            win_X_diff = mx-win_X
            win_Y_diff = my-win_Y
            window_float = True

        elif eventlistener.Event.get_event() is "leftclickup":
            win_X_diff = 0
            win_Y_diff = 0
            window_float = False

    if window_float:
        win_X = mx-win_X_diff
        win_Y = my-win_Y_diff

    # Window activation and deactivation
    if eventlistener.Event.get_event() is "leftclickdown":
        if eventlistener.Event.hovers(win_X, win_Y, win_W, win_H, "arrow"):
            window_active = True
        else: window_active = False
            




    # Create a window

    # Window
    graphics.Shape.rect(rgbcode.sub_window, coordinates, True, borderRadius = bdr_rad)
    
    """ Header """
    graphics.Shape.rect(rgbcode.header_active, (coordinates[0], coordinates[1], coordinates[2], header_H), borderRadius = bdr_rad)

    # Heading
    if window_active:
        graphics.Text.text(heading, (coordinates[0]+10, coordinates[1]+7), textFG = rgbcode.font)
    else:
        graphics.Text.text(heading, (coordinates[0]+10, coordinates[1]+7), textFG = rgbcode.font_secondary)


    """ Body """

    # Name of the project

    # Name entry
    name_entry_padding = 20

    graphics.Shape.rect(rgbcode.entry_BG, (coordinates[0]+name_entry_padding, coordinates[1]+50, coordinates[2]-(name_entry_padding*2), 20))
