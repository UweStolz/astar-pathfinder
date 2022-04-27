from typing import List

from Grid import Grid, Node


class Pathfinder:
    """
    A* Pathfinder
    """

    STRAIGHT_COST = 10
    DIAGONAL_COST = 14
    INITIAL_G_COST = 999999999
    open_nodes: List[Node] = list()
    closed_nodes: List[Node] = list()
    path: List[Node] = list()
    start_node: "Node|None" = None
    end_node: "Node|None" = None

    def __init__(self, grid: Grid):
        self.grid = grid
        pass

    def get_f_cost(self, node: Node) -> int:
        cost = node.g + node.h
        return cost

    def get_distance_cost(self, node_a: Node, node_b: Node) -> int:
        x_distance = abs(node_a.x - node_b.x)
        y_distance = abs(node_a.y - node_b.y)
        remaining = abs(x_distance - y_distance)

        distance = self.DIAGONAL_COST * \
            min(x_distance, y_distance) + self.STRAIGHT_COST * remaining

        return distance

    def get_lowest_fcost_node(self, nodes: List[Node]) -> "Node|None":
        lowest_fcost_node = None
        node_count = len(nodes)
        if node_count > 0:
            lowest_fcost_node = nodes[0]
            for i in range(1, node_count):
                node = nodes[i]
                if node.f < lowest_fcost_node.f:
                    lowest_fcost_node = node
                    pass
                pass
        return lowest_fcost_node

    def calculate_path(self, end_node: Node) -> List[Node]:
        path: List[Node] = list([end_node])
        current_node = end_node
        while current_node.previous_node:
            path.append(current_node.previous_node)
            current_node = current_node.previous_node
            pass
        path.reverse()
        return path

    def _add_to_neighbours(self, x: int, y: int, neighbours: List[Node]):
        neighbour = self.grid.get_node(x, y)
        if neighbour:
            neighbours.append(neighbour)
        pass

    def get_neighbours(self, node: Node) -> List[Node]:
        neighbours: List[Node] = list()
        x, y = node.x, node.y
        x_left = x - 1
        x_right = x + 1
        y_top = y - 1
        y_bottom = y + 1
        x_right_in_range = x_right <= self.grid.x_count
        x_left_in_range = x_left >= 0
        y_top_in_range = y_top >= 0
        y_bottom_in_range = y_bottom <= self.grid.y_count

        if x_left_in_range:
            # LEFT
            self._add_to_neighbours(x_left, y, neighbours)
        if x_right_in_range:
            # RIGHT
            self._add_to_neighbours(x_right, y, neighbours)

        if y_top_in_range:
            # TOP LEFT
            if x_left_in_range:
                self._add_to_neighbours(x_left, y_top, neighbours)
            # TOP CENTER
            self._add_to_neighbours(x, y_top, neighbours)
            # TOP RIGHT
            if x_right_in_range:
                self._add_to_neighbours(x_right, y_top, neighbours)

        if y_bottom_in_range:
            if x_left_in_range:
                # BOTTOM LEFT
                self._add_to_neighbours(x_left, y_bottom, neighbours)
            # BOTTOM CENTER
            self._add_to_neighbours(x, y_bottom, neighbours)
            if x_right_in_range:
                # BOTTOM RIGHT
                self._add_to_neighbours(x_right, y_bottom, neighbours)

        return neighbours

    def filter_walkables(self, nodes: List[Node]) -> List[Node]:
        walkable_nodes: List[Node] = list()
        for node in nodes:
            if node.walkable:
                walkable_nodes.append(node)
            else:
                self.closed_nodes.append(node)
        return walkable_nodes

    def find_path(self):
        self.open_nodes.clear()
        self.closed_nodes.clear()

        if self.start_node and self.end_node:
            self.open_nodes.append(self.start_node)

            for node in self.grid.nodes:
                node.previous_node = None
                node.g = self.INITIAL_G_COST
                node.f = self.get_f_cost(node)
                pass
            self.start_node.g = 0
            self.start_node.h = self.get_distance_cost(
                self.start_node,
                self.end_node
            )
            self.start_node.f = self.get_f_cost(self.start_node)

            while len(self.open_nodes) > 0:
                current_node = self.get_lowest_fcost_node(self.open_nodes)
                if current_node:
                    if current_node == self.end_node:
                        self.path = self.calculate_path(self.end_node)
                        return self.path
                    else:
                        self.open_nodes.remove(current_node)
                        self.closed_nodes.append(current_node)

                        neighbours = self.get_neighbours(current_node)
                        neighbours = self.filter_walkables(neighbours)

                        for neighbour_node in neighbours:
                            if neighbour_node in self.closed_nodes:
                                continue
                            tentative_g_cost = (
                                current_node.g +
                                self.get_distance_cost(
                                    current_node, neighbour_node)
                            )
                            if tentative_g_cost < neighbour_node.g:
                                neighbour_node.previous_node = current_node
                                neighbour_node.g = tentative_g_cost
                                neighbour_node.h = self.get_distance_cost(
                                    neighbour_node, self.end_node
                                )
                                neighbour_node.f = self.get_f_cost(
                                    neighbour_node
                                )
                                if neighbour_node not in self.open_nodes:
                                    self.open_nodes.append(neighbour_node)
                                    pass
                            pass
                else:
                    break
        pass

    pass
