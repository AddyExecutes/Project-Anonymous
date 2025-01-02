import pygame
import path
import rgbcode

# Initialize Pygame
pygame.init()


# Font setup
fontPath = path.font
italic_fontPath = path.italicfont

default_fontSize = "m"
textFG = rgbcode.font
textBG = None


small = 13
medium = 14
large = 16
xlarge = 18
xxlarge = 52

smallfont = pygame.font.Font(fontPath, small)
mediumfont = pygame.font.Font(fontPath, medium)
largefont = pygame.font.Font(fontPath, large)
xlargefont = pygame.font.Font(fontPath, xlarge)
xxlargefont = pygame.font.Font(fontPath, xxlarge)

italic_smallfont = pygame.font.Font(italic_fontPath, small)
italic_mediumfont = pygame.font.Font(italic_fontPath, medium)
italic_largefont = pygame.font.Font(italic_fontPath, large)
italic_xlargefont = pygame.font.Font(italic_fontPath, xlarge)
italic_xxlargefont = pygame.font.Font(italic_fontPath, xxlarge)

small_systemfont = pygame.font.SysFont(None, small)
medium_systemfont = pygame.font.SysFont(None, medium)
large_systemfont = pygame.font.SysFont(None, large)
xlarge_systemfont = pygame.font.SysFont(None, xlarge)
xxlarge_systemfont = pygame.font.SysFont(None, xxlarge)


class Text:


    @staticmethod
    def text(text: str, XY: tuple, sysfont: bool = False, italic: bool = False, fontSize: str = default_fontSize, textFG: tuple|str = textFG, textBG: tuple|str = textBG):
        import main

        if fontSize == "s":
            if italic:
                rendered_text = italic_smallfont.render(text, True, textFG, textBG)
            elif sysfont:
                rendered_text = small_systemfont.render(text, True, textFG, textBG)
            else:
                rendered_text = smallfont.render(text, True, textFG, textBG)
        
        elif fontSize == "m":
            if italic:
                rendered_text = italic_mediumfont.render(text, True, textFG, textBG)
            elif sysfont:
                rendered_text = medium_systemfont.render(text, True, textFG, textBG)
            else:
                rendered_text = mediumfont.render(text, True, textFG, textBG)
        
        elif fontSize == "l":
            if italic:
                rendered_text = italic_largefont.render(text, True, textFG, textBG)
            elif sysfont:
                rendered_text = large_systemfont.render(text, True, textFG, textBG)
            else:
                rendered_text = largefont.render(text, True, textFG, textBG)
        
        elif fontSize == "xl":
            if italic:
                rendered_text = italic_xlargefont.render(text, True, textFG, textBG)
            elif sysfont:
                rendered_text = xlarge_systemfont.render(text, True, textFG, textBG)
            else:
                rendered_text = xlargefont.render(text, True, textFG, textBG)
        
        elif fontSize == "xxl":
            if italic:
                rendered_text = italic_xxlargefont.render(text, True, textFG, textBG)
            elif sysfont:
                rendered_text = xxlarge_systemfont.render(text, True, textFG, textBG)
            else:
                rendered_text = xxlargefont.render(text, True, textFG, textBG)
        
        main.screen.blit(rendered_text, (XY[0], XY[1]))









class Shape:

    @staticmethod
    def rect(color: tuple | str, coordinates: tuple, border_bool: bool = False, border_color: tuple | str = rgbcode.border_line, borderWidth = 0, borderRadius = -1, top_left_radius = -1, top_right_radius = -1, bottom_left_radius = -1, bottom_right_radius = -1):
        import main

        pygame.draw.rect(main.screen, color, coordinates, borderWidth, borderRadius, top_left_radius, top_right_radius, bottom_left_radius, bottom_right_radius)

        if border_bool:
            pygame.draw.rect(main.screen, border_color, coordinates, 1, borderRadius, top_left_radius, top_right_radius, bottom_left_radius, bottom_right_radius)


    @staticmethod
    def circle(color: tuple | str, coordinates: tuple, radius: int | float, border_bool: bool = False):
        import main

        pygame.draw.circle(main.screen, color, coordinates, radius)

        if border_bool:
            pygame.draw.circle(main.screen, rgbcode.border_line, coordinates, radius, 1)


    @staticmethod
    def line(color: tuple | str, startXY: tuple, endXY: tuple, width = 1):
        import main

        pygame.draw.line(main.screen, color, (startXY[0], startXY[1]), (endXY[0], endXY[1]), width)



class Image:

    @staticmethod
    def show(image_path, XY: tuple, resize_bool: bool = False, resize_size: tuple = (), rotation_bool: bool = False, rotation_angle: int = 0):
        import main

        img = pygame.image.load(image_path)

        if resize_bool and resize_size != (): img = pygame.transform.scale(img, resize_size)
        if rotation_bool and rotation_angle != 0: img = pygame.transform.rotate(img, rotation_angle)

        main.screen.blit(img, (XY[0], XY[1]))