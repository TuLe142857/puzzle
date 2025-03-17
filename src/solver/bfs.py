from .abstract_solver import AbstractSolver
from .puzzle import Puzzle

class BFS(AbstractSolver):
    def __init__(self):
        super().__init__()

    def __str__(self):
        return "Breath First Search"

    def solve_puzzle(self, puzzle:Puzzle)->list[tuple[int, int]]:
        pass