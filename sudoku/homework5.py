############################################################
# CIS 521: Sudoku Homework 
############################################################

student_name = "Type your full name here."

############################################################
# Imports
############################################################

# Include your imports here, if any are used.



############################################################
# Section 1: Sudoku Solver
############################################################

def sudoku_cells():
    return [(i,j) for i in range(9) for j in range(9)]

def sudoku_arcs():
    arcs = []
    for i in range(9):
        for j in range(9):
            for k in range(9):
                if i != k:
                    arcs.append(((i,j),(k,j)))
                if j != k:
                    arcs.append(((i,j),(i,k)))
            for k in range(3):
                for l in range(3):
                    if i != i//3*3+k and j != j//3*3+l:
                        arcs.append(((i,j),(i//3*3+k,j//3*3+l)))
    return arcs

def read_board(path):
    board = {}
    with open(path, 'r') as f:
        for i in range(9):
            line = f.readline()
            for j in range(9):
                board[(i,j)] = {int(line[j])} if line[j] != '*' else set(range(1,10))
    return board

class Sudoku(object):

    CELLS = sudoku_cells()
    ARCS = sudoku_arcs()
    def __init__(self, board):
        self.board = board
        

    def get_values(self, cell):
        return self.board[cell]

    def remove_inconsistent_values(self, cell1, cell2):
        '''Remove values from cell1 that are not inequality constraints with cell2
         we ensure all cell1 and cell2 should be in the same row, column or box and has preset single value
         and cell2 should have single value already
        '''
    
        #inconsistent
        #1. in arcs
        #2. cell2 has single value to help cell1 to remove inconsistent value
        #3. cell2 value is a contained in cell1 so cell1 can remove it
        if (cell1, cell2) in self.ARCS and len(self.board[cell2]) == 1 and self.board[cell2].issubset(self.board[cell1]):
            self.board[cell1] -= self.board[cell2]
            return True
        return False


    def infer_ac3(self):
        #initialize the Queue with not assigned value cell1 and assigned value cell2
        queue = self.ARCS.copy()
        while queue:
            cell1, cell2 = queue.pop(0)
            if self.remove_inconsistent_values(cell1, cell2):
                for arc in self.ARCS:
                    if arc[1] == cell1 and arc[1] != cell2:
                        queue.append(arc)

             
    def infer_improved(self):
        extra_infer = True
        while extra_infer:
            self.infer_ac3()
            extra_infer = False
            for cell in self.CELLS:
                if len(self.board[cell]) > 1:
                    for val in self.board[cell]:
                        #check col (differnt row)
                        row, col = cell
                        
                        col_unique = True
                        for r in range(9):
                            if r != row and val in self.board[(r,col)]:
                                col_unique = False
                                break
                        if col_unique:
                            self.board[cell] = {val}
                            extra_infer = True
                            break

                        #check row (different col)
                        row_unique = True
                        for c in range(9):
                            if c != col and val in self.board[(row,c)]:
                                row_unique = False
                                break
                        if row_unique:
                            self.board[cell] = {val}
                            extra_infer = True
                            break
                        
                        #check box
                        box_unique = True
                        for r in range(row//3*3, row//3*3+3):
                            for c in range(col//3*3, col//3*3+3):
                                if r != row and c != col and val in self.board[(r,c)]:
                                    box_unique = False
                                    break
                        
                        if box_unique:
                            self.board[cell] = {val}
                            extra_infer = True
                            break

    def is_solved(self):
        for cell in self.CELLS:
            if len(self.board[cell]) != 1:
                return False
        return True

    def infer_with_guessing(self):
        self.infer_improved()

        for cell in self.CELLS:
            if len(self.board[cell]) > 1:
                for val in self.board[cell]:
                    board_copy = self.board.deepcopy()
                    self.board[cell] = {val}
                    self.infer_with_guessing()
                    if self.is_solved():
                        return
                    self.board = board_copy

        
                    
        



############################################################
# Section 1.5: Test
############################################################
# b = read_board("sudoku/medium1.txt")
# res = [
# ((0, 0), (0, 8)) in sudoku_arcs(),
#   ((0, 0), (8, 0)) in sudoku_arcs(),
#   ((0, 8), (0, 0)) in sudoku_arcs(),
#   ((0, 0), (2, 1)) in sudoku_arcs(),
#   ((2, 2), (0, 0)) in sudoku_arcs(),
#   ((2, 3), (0, 0)) in sudoku_arcs()]

# print(*res, sep = '\n')


# sudoku = Sudoku(read_board("sudoku/easy.txt")) # See below for a picture.
# sudoku.get_values((0, 3))
# for col in [0, 1, 4]:
#      removed = sudoku.remove_inconsistent_values((0, 3), (0, col))
#      print(removed, sudoku.get_values((0, 3)))
############################################################
# Section 2: Feedback
############################################################

# Just an approximation is fine.

feedback_question_1 = 5

feedback_question_2 = """
the infer and guessing part is hard to understand how to find out a way to solve it. I hope next time give more hints or example
"""

feedback_question_3 = """
it helps me a lot to understand the concept of CSP and how to solve it
"""
