# A* Pathfinder

Implementation of the [A *(star) search algorithm](https://en.wikipedia.org/wiki/A*_search_algorithm) in pygame with basic visualization.  

<img src="https://user-images.githubusercontent.com/41996712/165589377-97afb515-dfe4-4782-98dc-8e2bfa6a75c4.png" width="640" />


## Node

G = Cost from the start node  
  - Horizontal and vertical cost is `1`
  - Diagonal cost is `1.4`

H = Heuristic Cost from the start node to the goal node  
F = G + H

<img src="https://user-images.githubusercontent.com/41996712/164986512-3b42e367-a7c3-4094-87e5-ed3b5b95f4df.png" width="128" />

## Controls

Left mouse button - Set start node  
Right mouse button - Set end node  
Middle mouse button - Toggle walkability of node  

## Dependencies
- [Pygame](https://www.pygame.org/)
