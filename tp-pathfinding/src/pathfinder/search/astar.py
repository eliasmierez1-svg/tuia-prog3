from ..models.grid import Grid
from ..models.frontier import PriorityQueueFrontier
from ..models.solution import NoSolution, Solution
from ..models.node import Node


class AStarSearch:
    @staticmethod
    def search(grid: Grid) -> Solution:
        """Find path between two points in a grid using A* Search

        Args:
            grid (Grid): Grid of points

        Returns:
            Solution: Solution found
        """
        root = Node("", state=grid.initial, cost=0, parent=None, action=None)

        reached = {}
        reached[root.state] = root.cost

        frontera = PriorityQueueFrontier()
        frontera.add(root, priority=grid.heuristica(root) + root.cost)

        while True:
            if frontera.is_empty():
                return NoSolution(reached)

            nodo = frontera.pop()

            if grid.objective_test(nodo.state):
                return Solution(nodo, reached)

            for action in grid.actions(nodo.state):
                nuevo_estado = grid.result(nodo.state, action)
                nuevo_costo = nodo.cost + grid.individual_cost(nodo.state, action)

                if nuevo_estado not in reached or nuevo_costo < reached[nuevo_estado]:
                    reached[nuevo_estado] = nuevo_costo
                    nuevo_nodo = Node(action, state=nuevo_estado, cost=nuevo_costo, parent=nodo, action=action)
                    frontera.add(nuevo_nodo, priority=grid.heuristica(nuevo_nodo) + nuevo_nodo.cost)

        return NoSolution(reached)
