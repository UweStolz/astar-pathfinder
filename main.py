import pygame
import pygame.freetype
from sys import exc_info, exit
from asyncio import run, sleep
from traceback import print_exception
from pygame import Rect, mouse, event, display, time
from pygame.ftfont import Font
from pygame.constants import DOUBLEBUF, QUIT, MOUSEBUTTONDOWN
from pygame.surface import Surface

from Colors import WHITE, WHITE_10, BLACK
from Grid import Grid
from Fonts import FONTS
from Node import Node
from NodeSprite import NodeSprite
from Pathfinder import Pathfinder
from PathVisualizer import PathVisualizer
from callbacks import add_start_node, add_end_node, toggle_node_walkable_state

grid = Grid()
pathfinder = Pathfinder(grid)
pathVisualizer = PathVisualizer(pathfinder)


WINDOW_WIDTH = 960
WINDOW_HEIGHT = 540


def draw_initial_grid(surface: Surface):
    BLOCK_SIZE = 60

    for index_x, x in enumerate(range(0, WINDOW_WIDTH, BLOCK_SIZE)):
        for index_y, y in enumerate(range(0, WINDOW_HEIGHT, BLOCK_SIZE)):
            rect = Rect(x, y, BLOCK_SIZE, BLOCK_SIZE)
            sprite = NodeSprite(
                WHITE,
                WHITE_10,
                rect,
                outline=BLACK,
                lmb_callback=add_start_node(pathfinder, pathVisualizer),
                rmb_callback=add_end_node(pathfinder, pathVisualizer),
                mmb_callback=toggle_node_walkable_state(
                    pathfinder, pathVisualizer
                )
            )
            grid.nodes.append(
                Node(
                    index_x,
                    index_y,
                    True,
                    sprite
                )
            )
            grid.sprites.add(sprite)
            grid.y_count += 1
            pass
        grid.x_count += 1
        grid.sprites.draw(surface)
    pass


def init_pygame():
    size = WINDOW_WIDTH, WINDOW_HEIGHT
    flags = DOUBLEBUF
    pygame.init()
    display.set_caption("A* Pathfinding")
    event.set_allowed([QUIT, MOUSEBUTTONDOWN])
    FONTS.primary_font = Font(None, FONTS.primary_font_size)
    FONTS.secondary_font = Font(None, FONTS.secondary_font_size)
    surface = display.set_mode(size, flags, 24)
    surface.fill(WHITE)
    pass


async def main():
    init_pygame()
    FPS = 60
    SURFACE = display.get_surface()
    CLOCK = time.Clock()
    draw_initial_grid(SURFACE)

    while True:
        events = pygame.event.get()
        for event in events:
            if event.type == QUIT:
                pygame.quit()
                exit()

        mouse_position = mouse.get_pos()
        grid.sprites.update(events, mouse_position, grid)
        grid.sprites.draw(SURFACE)

        if pathfinder.path and len(pathfinder.path) > 0:
            pathVisualizer.draw_path()

        CLOCK.tick(FPS)
        display.flip()
        await sleep(0)


if __name__ == '__main__':
    try:
        run(main())
    except Exception as e:
        tb = exc_info()[2]
        print_exception(e.__class__, e, tb)
    pygame.quit()
    exit()
