class _InFile_: # Don't use this class outside this file

    def mouse_pos() -> tuple :

        from main import pygame

        # Mouse coordinates distributer
        mx = pygame.mouse.get_pos()[0]
        my = pygame.mouse.get_pos()[1]

        return (mx, my)

class Event:

    def get_event():

        from main import pygame, event


        # Checks if Quit 
        if event.type == pygame.QUIT:
            return "quit"

        # Checks if Key Pressed


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

        return _InFile_.mouse_pos()

    
    @staticmethod
    def hovers(X: int, Y: int, W: int, H: int) -> bool:

        mx, my = _InFile_.mouse_pos()

        return X <= mx <= X + W and Y <= my <= Y + H