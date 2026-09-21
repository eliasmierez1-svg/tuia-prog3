from ..models.grid import Grid
from ..models.frontier import PriorityQueueFrontier
from ..models.solution import NoSolution, Solution
from ..models.node import Node


class UniformCostSearch:
    @staticmethod
    def search(grid: Grid) -> Solution:
        """Find path between two points in a grid using Uniform Cost Search

        Args:
            grid (Grid): Grid of points

        Returns:
            Solution: Solution found
        """
        # Initialize root node
        root = Node("", state=grid.initial, cost=0, parent=None, action=None)

        # Initialize frontier with the root node
        frontera = PriorityQueueFrontier()
        frontera.add(root)

        # Initialize reached with the initial state
        reached = {}
        reached[root.state] = root.cost
        
        while True:
            if frontera.is_empty():
                return NoSolution(reached)

            nodo1 = frontera.pop()

            if grid.objective_test(nodo1.state):
                return Solution(nodo1, reached)
            
            for a in grid.actions(nodo1.state):
                resultado = grid.result(nodo1.state, a)
                costo = nodo1.cost + grid.individual_cost(nodo1.state, a)   

                if resultado not in reached or costo < reached[resultado]:
                    hijo = Node("", resultado, costo, nodo1, a)
                    reached[resultado] = costo
                    frontera.add(hijo, costo)  
        return NoSolution(reached)
                                
