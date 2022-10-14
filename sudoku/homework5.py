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

def sudoku_arcs_helper():
    #for every cell, check the row, column and the box
    arcs, rowarcs, colarcs, boxarcs = set(), set(), set(), set()
    for i in range(9):
        for j in range(9):
            for k in range(9):
                if i != k:
                    arcs.add(((i,j),(k,j)))
                    rowarcs.add(((i,j),(i,k)))
                if j != k:
                    arcs.add(((i,j),(i,k)))
                    colarcs.add(((i,j),(k,j)))
            for k in range(3):
                for l in range(3):
                    if i != i//3*3+k and j != j//3*3+l:
                        arcs.add(((i,j),(i//3*3+k,j//3*3+l)))
                        boxarcs.add(((i,j),(i//3*3+k,j//3*3+l)))
    return list(arcs), list(rowarcs), list(colarcs), list(boxarcs)

def sudoku_arcs():
    return sudoku_arcs_helper()[0]

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
    ARCS, ROWARCS, COLARCS, BOXARCS = sudoku_arcs_helper()

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
        if  len(self.board[cell2]) > 1:
            return False

        if not self.board[cell2].issubset(self.board[cell1]):
            return False

        self.board[cell1] -= self.board[cell2]

        return True


    def infer_ac3(self):
        #initialize the Queue with not assigned value cell1 and assigned value cell2
        queue = self.ARCS.copy()
        while queue:
            cell1, cell2 = queue.pop(0)
            if self.remove_inconsistent_values(cell1, cell2):
                if len(self.board[cell1]) == 0:
                    return False
                for arc in self.ARCS:
                    if arc[1] == cell1 and arc[1] != cell2:
                        queue.append(arc)

             
    def infer_improved(self):
        
        

    def infer_with_guessing(self):
        pass
        # self.infer_improved()

        # for cell in self.CELLS:
        #     if len(self.board[cell]) > 1:
        #         for val in self.board[cell]:
        #             board_copy = self.board.deepcopy()
        #             board_copy[cell] = {val}
        #             sudoku_copy = Sudoku(board_copy)
        #             sudoku_copy.infer_with_guessing()
        #             if all(len(sudoku_copy.board[cell]) == 1 for cell in self.CELLS):
        #                 self.board = sudoku_copy.board
        #                 return 
        
                    
        



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
