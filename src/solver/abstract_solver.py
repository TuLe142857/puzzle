from abc import ABC, abstractmethod
from solver.puzzle import Puzzle

class AbstractSolver(ABC):
    def __init__(self):
        super().__init__()
        
    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def solve_puzzle(self, puzzle:Puzzle)->list[tuple[int, int]]:
        pass

    