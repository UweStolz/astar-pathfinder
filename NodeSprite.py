from multiprocessing import Event
from typing import List, Tuple
from pygame import sprite, Color, Surface
from pygame.constants import MOUSEBUTTONDOWN
from pygame.event import Event
from pygame.rect import Rect
from Colors import BLACK

LEFT_MOUSE_BUTTON = 1
MIDDLE_MOUSE_BUTTON = 2
RIGHT_MOUSE_BUTTON = 3


class NodeSprite(sprite.Sprite):

    def __init__(self, color: Color, color_hover: Color, rect: Rect, lmb_callback=None, rmb_callback=None, mmb_callback=None, outline: "Color|None" = None):
        super().__init__()
        tmp_rect = Rect(0, 0, *rect.size)
        self.org = self._create_image(color, outline, tmp_rect)
        self.unwalkable = self._create_image(BLACK, None, tmp_rect)
        self.hover = self._create_image(color_hover, outline, tmp_rect)
        self.image = self.org
        self.rect = rect
        self.lmb_callback = lmb_callback
        self.rmb_callback = rmb_callback
        self.mmb_callback = mmb_callback

    def _create_image(self, color: Color, outline: "Color|None", rect: Rect):
        img = Surface(rect.size)
        if outline:
            img.fill(outline)
            img.fill(color, rect.inflate(-4, -4))
        else:
            img.fill(color)
        return img

    def update(self, events: List[Event], mouse_position: Tuple[int, int], grid):
        if self.rect:
            hit = self.rect.collidepoint(mouse_position)
            node = grid.get_node_for_sprite(self)
            if node and node.walkable:
                self.image = self.hover if hit else self.org

            for event in events:
                if event.type == MOUSEBUTTONDOWN and hit:
                    if event.button == LEFT_MOUSE_BUTTON:
                        if self.lmb_callback:
                            self.lmb_callback(self, node)
                        pass
                    elif event.button == MIDDLE_MOUSE_BUTTON:
                        if self.mmb_callback:
                            self.mmb_callback(self, node)
                        pass
                    elif event.button == RIGHT_MOUSE_BUTTON:
                        if self.rmb_callback:
                            self.rmb_callback(self, node)
                        pass
                    break
    pass
