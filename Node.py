from dataclasses import dataclass

from NodeSprite import NodeSprite


@dataclass(eq=False)
class Node:
    """
    G = Cost from the start node
        - Horizontal and vertical cost is `10`
        - Diagonal cost is `14`

    H = Heuristic Cost from the start node to the goal node\n
    F = G + H
    """

    x: int
    y: int
    walkable: bool
    g: int
    f: int
    h: int
    sprite: NodeSprite
    previous_node: "Node|None"

    def __init__(self, x: int, y: int, walkable: bool, sprite: NodeSprite, previous_node: "Node|None" = None):
        self.x = x
        self.y = y
        self.walkable = walkable
        self.g = 0
        self.h = 0
        self.f = 0
        self.sprite = sprite
        self.previous_node = previous_node
        pass

    def __hash__(self):
        return hash((self.x, self.y))

    def __eq__(self, other):
        return self.x == other.x \
            and self.y == other.y
