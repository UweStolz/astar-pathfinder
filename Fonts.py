from pygame.ftfont import Font


class FontsProxy:
    primary_font_size: int = 24
    secondary_font_size: int = 18
    primary_font: Font
    secondary_font: Font
    pass


FONTS = FontsProxy()
