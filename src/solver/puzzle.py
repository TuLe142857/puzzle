import math
import random

# Gia tri cua o trong
BLANK_CELL = -1

# vector tuong ung cac cach di duyen
UP = (-1, 0)
DOWN = (1, 0)
LEFT = (0, -1)
RIGHT = (0, 1)

class Puzzle:
    '''
    Hello!

    cells: list[list[int]]
    
        columns 
            0 1 2 3 4 
     row
        0  
        2
        3
        4
   
    '''
    def __init__(self, rows, columns):

        # kich thuoc 
        self.rows = rows
        self.columns = columns

        # gia tri cua cac o
        self.cells = [[r*columns + c + 1 for c in range(columns)] for r in range(rows)]

        # mac dinh o trong o vi tri cuoi cung
        self.cells[rows-1][columns-1] = BLANK_CELL

        # luu lai vi tri o trong de tien dung trong luc di chuyen o trong
        # (su dung trong ham simulate_direction/execute_direction)
        self.blank_cells_index = [rows-1,columns-1]

    def shuffle(self)->None:
        for i in range(self.rows):
            for j in range(self.columns):
                k = random.randint(i*self.columns + j, self.rows*self.columns-1)
                r = k // self.columns
                c = k % self.columns
                self.cells[i][j], self.cells[r][c] = self.cells[r][c], self.cells[i][j]
        self.blank_cells_index[0], self.blank_cells_index[1] = self.where(BLANK_CELL)

    def where(self, value)->tuple[int, int]:
        '''
        tra ve index(row, column) cua o co gia tri tuong ung
        tra ve None neu khong tim thay
        '''
        for i in range(self.rows):
            for j in range(self.columns):
                if(value == self.cells[i][j]):
                    return (i, j)
        return None

    def clone(self, value)->'Puzzle':
        p = Puzzle(self.rows, self.columns)
        for i in range(self.rows):
            for j in range(self.columns):
                p.cells[i][j] = self.cells[i][j]
        p.blank_cells_index[0], p.blank_cells_index[1] = self.where(BLANK_CELL)
        return p

    def __eq__(self, other:'Puzzle')->bool:
        if not (self.rows == other.rows and self.columns == other.columns):
            raise RuntimeError("Can not compare different puzzle (not same size)")
        for i in range(self.rows):
            for j in range(self.columns):
                if(self.cells[i][j] != other.cells[i][j]):
                    return False
        return True
    
    def __ne__(self, other:'Puzzle')->bool:
        if not (self.rows == other.rows and self.columns == other.columns):
            raise RuntimeError("Can not compare different puzzle (not same size)")
        for i in range(self.rows):
            for j in range(self.columns):
                if(self.cells[i][j] != other.cells[i][j]):
                    return True
        return False

    def possible_moves(self)->list[tuple[int, int]]:
        moves = []
        if self.blank_cells_index[0] != 0:
            moves.append(UP)
        if self.blank_cells_index[0] != self.rows - 1:
            moves.append(DOWN)
        if self.blank_cells_index[1] != 0:
            moves.append(LEFT)
        if self.blank_cells_index[1] != self.columns - 1:
            moves.append(RIGHT)
        return moves

    def simulate_move(self, direction)->'Puzzle':
        '''
        Tra ve moi puzzle la ket qua cua cach di chuyen
        Khong thay doi trang thai puzzle
        '''
        result = self.clone()
        result.execute_move(direction)

        return result

    def execute_move(self, direction)->None:
        '''
        Thuc thi di chuyen o trong theo huong cho truoc(direction)
        Gay thay doi trang thai puzzle
        '''
        if direction not in [UP, DOWN, LEFT, RIGHT]:
            raise RuntimeError("Invalid direction")

        blank_cell = self.blank_cells_index
        swap_cell = [blank_cell[0] + direction[0], blank_cell[1] + direction[1]]
        if not ( (0 <= swap_cell[0] < self.rows)  and (0 <= swap_cell[1] < self.columns)):
            return None
        
        
        self.cells[blank_cell[0]][blank_cell[1]], self.cells[swap_cell[0]][swap_cell[1]] = \
            self.cells[swap_cell[0]][swap_cell[1]], self.cells[blank_cell[0]][blank_cell[1]]

        self.blank_cells_index = swap_cell
        

    def __str__(self)->str:
        s = ""
        max_width = math.ceil(math.log(self.rows*self.columns -1, 10))
        for i in range(self.rows):
            line = "|"
            for j in range(self.columns):
                if self.cells[i][j] != BLANK_CELL:
                    str_value = str(self.cells[i][j])
                    line += " "*(max_width - len(str_value)) + str_value + '|' 
                else:
                    line += "_" * max_width + "|"
            line += '\n'
            s += line
        return s



# p = Puzzle(15, 20)
# print(p)
# print(p.possible_moves())

# p.execute_move(DOWN)
# print(p)

# p.execute_move(UP)
# print(p)

# p.execute_move(LEFT)
# print(p)

# p.execute_move(RIGHT)
# print(p)

# p.execute_move(DOWN)
# print(p)

# p.execute_move(UP)
# print(p)
# p.shuffle()

# print(p)
# print(p.blank_cells_index)
# print(p.possible_moves())