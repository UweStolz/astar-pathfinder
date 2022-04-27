from typing import List
from pygame import Surface, display

from Fonts import FONTS
from Colors import BLACK, GREEN, WHITE
from Node import Node
from Pathfinder import Pathfinder


class PathVisualizer:
    def __init__(self, pathfinder: Pathfinder) -> None:
        self.pathfinder = pathfinder
        pass

    def draw_path(self) -> None:
        neighbours_of_path: List[Node] = list()
        surface = display.get_surface()
        primary_font = FONTS.primary_font
        secondary_font = FONTS.secondary_font
        tl_padding = 4
        br_padding = 20

        for node in self.pathfinder.path:
            # Get neighbors for path
            neighbours = self.pathfinder.get_neighbours(node)
            walkable_neighbours = self.pathfinder.filter_walkables(neighbours)
            calculated_neighbours = [
                item for item in walkable_neighbours if item.g != self.pathfinder.INITIAL_G_COST
            ]
            neighbours_of_path.extend(calculated_neighbours)

            if node.sprite.rect:
                img = Surface(node.sprite.rect.size)
                img.fill(GREEN)
                surface.blit(img, node.sprite.rect)
            pass

        for neighbour in neighbours_of_path:
            if neighbour.sprite.rect:
                # CENTER
                f_cost_text: Surface = primary_font.render(
                    str(neighbour.f),
                    True,
                    BLACK
                )
                surface.blit(
                    f_cost_text,
                    (
                        neighbour.sprite.rect.centerx - f_cost_text.get_width() // 2,
                        neighbour.sprite.rect.centery - f_cost_text.get_height() // 2
                    ),
                )

                # TOP LEFT
                g_cost_text: Surface = secondary_font.render(
                    str(neighbour.g),
                    True,
                    BLACK
                )
                top_left_cords = neighbour.sprite.rect.topleft
                surface.blit(
                    g_cost_text,
                    (
                        top_left_cords[0] + tl_padding,
                        top_left_cords[1] + tl_padding
                    ),
                )

                # BOTTOM RIGHT
                h_cost_text: Surface = secondary_font.render(
                    str(neighbour.h),
                    True,
                    BLACK
                )
                bottom_right_cords = neighbour.sprite.rect.bottomright
                surface.blit(
                    h_cost_text,
                    (
                        bottom_right_cords[0] - br_padding,
                        bottom_right_cords[1] - br_padding
                    ),
                )
            pass

        pass
