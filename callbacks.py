from NodeSprite import NodeSprite
from Node import Node
from Pathfinder import Pathfinder
from PathVisualizer import PathVisualizer


def initiate_path_calculation(pathfinder: Pathfinder, pathVisualizer: PathVisualizer):
    if pathfinder.start_node and pathfinder.end_node:
        pathfinder.path.clear()
        path = pathfinder.find_path()
        if path and len(path) > 0:
            pathVisualizer.draw_path()
            pass
        pass
    pass


def add_start_node(pathfinder: Pathfinder, pathVisualizer: PathVisualizer):
    def fn(_node_sprite: NodeSprite, node: Node):
        if node.walkable:
            pathfinder.start_node = node
            initiate_path_calculation(pathfinder, pathVisualizer)
        pass
    return fn


def add_end_node(pathfinder: Pathfinder, pathVisualizer: PathVisualizer):
    def fn(_node_sprite: NodeSprite, node: Node):
        if node.walkable:
            pathfinder.end_node = node
            initiate_path_calculation(pathfinder, pathVisualizer)
        pass
    return fn


def toggle_node_walkable_state(pathfinder: Pathfinder, pathVisualizer: PathVisualizer):
    def fn(node_sprite: NodeSprite, node: Node):
        if node:
            node.walkable = not node.walkable
            node_sprite.image = node_sprite.unwalkable if not node.walkable else node_sprite.org
            initiate_path_calculation(pathfinder, pathVisualizer)
        pass
    return fn
