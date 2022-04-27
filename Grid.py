from typing import List
from pygame import sprite

from Node import Node
from NodeSprite import NodeSprite


class Grid:
    x_count: int = 0
    y_count: int = 0
    nodes: List[Node] = list()
    sprites = sprite.Group()

    def get_node_for_sprite(self, sprite: NodeSprite) -> "Node|None":
        node: "Node|None" = None
        for tmp_node in self.nodes:
            if tmp_node.sprite == sprite:
                node = tmp_node
                break
        return node

    def get_node(self, x: int, y: int) -> "Node|None":
        node: "Node|None" = None
        for tmp_node in self.nodes:
            if tmp_node.x == x and tmp_node.y == y:
                node = tmp_node
                break
        return node

    pass
