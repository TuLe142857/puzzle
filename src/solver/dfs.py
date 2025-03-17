from .abstract_solver import AbstractSolver
from .puzzle import Puzzle

class DFS(AbstractSolver):
    def __init__(self):
        super().__init__()

    def __str__(self):
        pass

    def solve_puzzle(self, puzzle:Puzzle)->list[tuple[int, int]]:
        pass