class Event:

    def get_event():

        from main import pygame, event

        # Checks if Quit 
        if event.type == pygame.QUIT:
            return "quit"


        '''
        Guide:
        1 - left click
        2 - middle click
        3 - right click
        4 - scroll up
        5 - scroll down
        '''

        # Checks if mouse button down
        if event.type == pygame.MOUSEBUTTONDOWN:

            # Addressing the left click
            if event.button == 1:
                return "leftclickdown"
            
            elif event.button == 2:
                return "middleclickdown"

            elif event.button == 3:
                return "rightclickdown"
        
        # Checks if mouse button up
        elif event.type == pygame.MOUSEBUTTONUP:

            # Addressing the left click
            if event.button == 1:
                return "leftclickup"
            
            elif event.button == 2:
                return "middleclickup"

            elif event.button == 3:
                return "rightclickup"
        
        # Checks for Keyboard input
        elif event.type == pygame.KEYDOWN:
            return event.unicode

    def mouse_pos() -> tuple :

        from main import pygame

        global mx, my

        # Mouse coordinates distributer
        mx = pygame.mouse.get_pos()[0]
        my = pygame.mouse.get_pos()[1]

        return (mx, my)

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
    
    @staticmethod
    def hovers(X: int, Y: int, W: int, H: int, cursortype: str) -> bool:

        from main import pygame

        if mx >= X and mx <= X+W and my >= Y and my <= Y+H:

            # Customizing the cursor
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

            return True

        else:
            
            # Setting the cursor to defualt (arrow) 
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

            return False