from ..models.grid import Grid
from ..models.frontier import PriorityQueueFrontier
from ..models.solution import NoSolution, Solution
from ..models.node import Node


class GreedyBestFirstSearch:
    @staticmethod
    def search(grid: Grid) -> Solution:
        """Find path between two points in a grid using Greedy Best First Search

        Args:
            grid (Grid): Grid of points

        Returns:
            Solution: Solution found
        """
        # Initialize root node
        root = Node("", state=grid.initial, cost=0, parent=None, action=None)

        # Initialize reached with the initial state
        reached = {}
        reached[root.state] = root.cost

        # Initialize frontier with the root node
        frontera = PriorityQueueFrontier()
        frontera.add(root, priority=grid.heuristica(root))
        
        while True:
            if frontera.is_empty():
                return NoSolution(reached)

            nodo = frontera.pop()

            if grid.objective_test(nodo.state):
                return Solution(nodo, reached)

            for action in grid.actions(nodo.state):
                new_state = grid.result(nodo.state, action)
                new_cost = nodo.cost + grid.individual_cost(nodo.state, action)

                if new_state not in reached or new_cost < reached[new_state]:
                    reached[new_state] = new_cost
                    new_node = Node(action, state=new_state, cost=new_cost, parent=nodo, action=action)
                    frontera.add(new_node, priority=grid.heuristica(new_node))

        return NoSolution(reached)
