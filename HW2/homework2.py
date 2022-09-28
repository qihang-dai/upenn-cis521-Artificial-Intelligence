############################################################
# CIS 521: Uninformed Search Homework
############################################################

student_name = "Qihang Dai"

############################################################
# Imports
############################################################

# Include your imports here, if any are used.

import math, random, copy

############################################################
# Section 1: N-Queens
############################################################

def num_placements_all(n):
    up = math.factorial(n * n)
    down = math.factorial(n * n - n) * math.factorial(n)
    return up/down

def num_placements_one_per_row(n):
    return n ** n

def n_queens_valid(board):
    SetC = set()
    SetD = set()
    SetD2 = set()

    for r in range(len(board)):
        c = board[r]
        diag = c - r
        diag2 = c + r
        if(c in SetC or diag in SetD or diag2 in SetD2): return False
        SetC.add(c)
        SetD.add(diag)
        SetD2.add(diag2)
    return True


def n_queens_solutions(n):
    return [list(v) for v in n_queens_helper(n, [])]

def n_queens_helper(n, board):
    # reach the end of row, return a value (boot of the recursive).
    if len(board) == n:
        yield board
    for c in range(n): 
        # place every col in the first row
        board.append(c) 
        if n_queens_valid(board): # if valid, recursive
            for v in n_queens_helper(n,board): #yield return every value
                yield v
        board.pop() #dont stack the old values.

    

############################################################
# Section 2: Lights Out
############################################################

class LightsOutPuzzle(object):

    def __init__(self, board):
        self.board = board
        self.rowMax = len(board)
        self.colMax = len(board[0])
        self.move = [[0, 1], [0, -1], [1, 0], [-1, 0]]

    def get_board(self):
        return self.board

    def perform_move(self, row, col):
        self.board[row][col] = not self.board[row][col]
        for m in self.move:
            r = row + m[0]
            c = col + m[1]
            if r < 0 or c < 0 or r >= self.rowMax or c >= self.colMax: 
                continue
            self.board[r][c] = not self.board[r][c]

    def scramble(self):
        for r in range(self.rowMax):
            for c in range(self.colMax):
                if(random.random() < 0.5):
                    self.perform_move(r, c)

    def is_solved(self):
        for r in range(self.rowMax):
            for c in range(self.colMax):
                if self.board[r][c] == True:
                    return False
        return True

    def copy(self):
        tmp = copy.deepcopy(self.board)
        return LightsOutPuzzle(tmp)

    def successors(self):
        for r in range(self.rowMax):
            for c in range(self.colMax):
                tmp = self.copy()
                tmp.perform_move(r, c)
                m = (r, c)
                yield m, tmp


    def find_solution(self):        
        q = [self]
        stateToMove = {self: []}

        while q:
            now = q.pop()

            if now.is_solved():
                move = stateToMove[now]
                # if move == [] : move = [(0, 0)]
                return move
            
            for move, nextState in now.successors():
                if nextState in stateToMove: 
                    #skip if this state is already there
                    continue
                # store the moves. tuples can be add up
                stateToMove[nextState] = stateToMove[now] + [move]
                q[:0] = [nextState]
        
        
def create_puzzle(rows, cols):
    b = [[False for j in range(cols)] for i in range(rows)]
    return LightsOutPuzzle(b)


############################################################
# Section 3: Linear Disk Movement
############################################################



def nextSteps(A):
    for i in range(len(A)):
        val = A[i]
        if val >= 0:
            if i + 1 < len(A) and A[i + 1] == -1:
                tmpA = list(A)
                tmpA[i] = -1
                tmpA[i + 1] = val
                move = (i, i + 1)
                newState = tuple(tmpA)
                yield  move, newState
            elif(i < len(A) - 2 and A[i + 1] >= 0 and A[i + 2] == -1):
                tmpA = list(A)
                tmpA[i] = -1
                tmpA[i + 2] = val
                move = (i, i + 2)
                newState = tuple(tmpA)
                yield  move, newState
            elif(i > 0 and A[i - 1] == -1):
                tmpA = list(A)
                tmpA[i] = -1
                tmpA[i - 1] = val
                move = (i, i - 1)
                newState = tuple(tmpA)
                yield  move, newState
            elif(i > 1 and A[i - 2] >= 0 and A[i - 2] == -1):
                tmpA = list(A)
                tmpA[i] = -1
                tmpA[i - 2] = val
                move = (i, i - 2)
                newState = tuple(tmpA)
                yield  move, newState

def solve(A):        
    q = [tuple(A)]
    res = A[::-1]
    stateToMove = {tuple(A): []}

    while q:
        now = q.pop()

        if now == tuple(res):
            move = stateToMove[now]
            # if move == [] : move = [(0, 0)]
            print(move)
            return move
        
        for move, nextState in nextSteps(now):
            if nextState in stateToMove: 
                #skip if this state is already there
                continue
            # store the moves. tuples can be add up
            stateToMove[nextState] = stateToMove[now] + [move]
            q[:0] = [nextState]

    

def solve_identical_disks(length, n):
    init = [1 if i < n else -1 for i in range(length) ]
    return solve(init)

def solve_distinct_disks(length, n):
    init = [i if i < n else -1 for i in range(length) ]
    return solve(init)

solve_identical_disks(4, 2)
solve_identical_disks(5, 2)
solve_identical_disks(4, 3)
solve_identical_disks(5, 3)
############################################################
# Section 4: Feedback
############################################################

feedback_question_1 = """
10 hours from morning to night
"""

feedback_question_2 = """
its tricky to know how to use yiled in an recrusive way
"""

feedback_question_3 = """
good python practice... I am java main.
"""
