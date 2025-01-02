import graphics
import rgbcode

sub_windows = []

def create_with(coordinates: tuple, heading: str, bdr_rad: int = 3):

    # Window
    graphics.Shape.rect(rgbcode.sub_window, coordinates, True, borderRadius = bdr_rad)
    
    # Header
    graphics.Shape.rect(rgbcode.header, (coordinates[0], coordinates[1], coordinates[2], 30), borderRadius = bdr_rad)

    # Heading
    graphics.Text.text(heading, (coordinates[0]+10, coordinates[1]+7), textFG = rgbcode.font_secondary)
