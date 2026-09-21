from ..models.grid import Grid
from ..models.frontier import StackFrontier
from ..models.solution import NoSolution, Solution
from ..models.node import Node


class DepthFirstSearch:
    @staticmethod
    def search(grid: Grid) -> Solution:
        """Find path between two points in a grid using Depth First Search

        Args:
            grid (Grid): Grid of points

        Returns:
            Solution: Solution found
        """

        root = Node("", state=grid.initial, cost=0, parent=None, action=None)
        expanded = {}
        expanded[root.state] = True

        nodo = root

        if grid.objective_test(nodo.state):
            return Solution(nodo, expanded)
        frontera = StackFrontier()
        frontera.add(nodo)

        while True:
            if frontera.is_empty():
                return NoSolution(expanded)
            nodo1 = frontera.remove()
            for a in grid.actions(nodo1.state):
                resultado = grid.result(nodo1.state, a)
                if resultado not in expanded:
                    hijo = Node("", resultado, nodo1.cost + grid.individual_cost(nodo1.state, a), nodo1, a)
                    expanded[resultado] = True
                    if grid.objective_test(resultado):
                        return Solution(hijo, expanded)
                    frontera.add(hijo)
        return NoSolution(expanded)