############################################################
# CIS 521: Informed Search Homework
############################################################

student_name = "Type your full name here."

############################################################
# Imports
############################################################

# Include your imports here, if any are used.
from queue import PriorityQueue
import random
import math


############################################################
# Section 1: Tile Puzzle
############################################################

def create_tile_puzzle(rows, cols):
    board = []
    count = 1
    for row in range(rows):
        board.append([])
        for col in range(cols):
            board[row].append(count)
            count += 1
    board[rows - 1][cols - 1] = 0
    return TilePuzzle(board)


class TilePuzzle(object):
    
    # Required
    def __init__(self, board):
        self.board = board
        self.rows = len(board)
        self.cols = len(board[0])
        for i in range(self.rows):
            for j in range(self.cols):
                if board[i][j] == 0:
                    self.r = i
                    self.c = j

    def get_board(self):
        return self.board

    def perform_move(self, direction):
        if direction == 'up' and self.r > 0:
            self.board[self.r][self.c] = self.board[self.r - 1][self.c]
            self.board[self.r - 1][self.c] = 0
            self.r -= 1
        elif direction == 'down' and self.r < self.rows - 1:
            self.board[self.r][self.c] = self.board[self.r + 1][self.c]
            self.board[self.r + 1][self.c] = 0
            self.r += 1
        elif direction == 'left' and self.c > 0:
            self.board[self.r][self.c] = self.board[self.r][self.c - 1]
            self.board[self.r][self.c - 1] = 0
            self.c -= 1
        elif direction == 'right' and self.c < self.cols - 1:
            self.board[self.r][self.c] = self.board[self.r][self.c + 1]
            self.board[self.r][self.c + 1] = 0
            self.c += 1
        else:
            return False
        # print(self.get_board())
        return True


    def scramble(self, num_moves):
        moveCount = 0
        while moveCount < num_moves:
            direction = random.choice(['up', 'down', 'left', 'right'])
            if self.perform_move(direction):
                moveCount += 1


    def is_solved(self):
        starter = create_tile_puzzle(self.rows, self.cols)
        return self.board == starter.board

    def copy(self):
        return TilePuzzle([row[:] for row in self.board]) 

    def successors(self):
        for move in ['up', 'down', 'left', 'right']:
            newBoard = self.copy()
            if newBoard.perform_move(move):
                print(newBoard.get_board())
                yield (move, newBoard)

    # Required
    def find_solutions_iddfs(self):
        limit = 1
        while True:
            solved = False
            for solution in self.iddfs_helper(limit, []):
                solved = True
                yield solution
            if solved:
                break
            limit += 1
    
    def iddfs_helper(self, limit, moves):
        if self.is_solved():
            yield moves
        if limit > 0:
            for move, next in self.successors():
                yield from next.iddfs_helper(limit - 1, moves + [move])
    

    def manhattan_distance(self):
        distance = 0
        for row in range(self.rows):
            for col in range(self.cols):
                if self.board[row][col] != 0:
                    distance += abs(row - (self.board[row][col] - 1) // self.cols) + abs(col - (self.board[row][col] - 1) % self.cols)
        return distance

    def as_tuple(self):
        return tuple(tuple(row) for row in self.board)

    # Required
    def find_solution_a_star(self):
        frontier = PriorityQueue()
        frontier.put((self.manhattan_distance(), 0, [], self))
        explored = set()
        while frontier:
            h, g, moves, board = frontier.get()
            if board.as_tuple() in explored:
                continue
            explored.add(board.as_tuple())
            if board.is_solved():
                return moves
            for move, next in board.successors():
                if next.as_tuple() not in explored:
                    frontier.put((next.manhattan_distance() + g + 1, g + 1, moves + [move], next))

############################################################
# Section 2: Grid Navigation
############################################################

class GridNavigation(object):
    
    # Required
    def __init__(self, scene, start, goal):
        self.scene = scene 
        self.rows = len(scene)
        self.cols = len(scene[0])
        self.start = start
        self.row = start[0]
        self.col = start[1]
        self.goal = goal
        
    
    def perform_move(self, direction):
        if direction == 'up' and self.row > 0 and self.scene[self.row - 1][self.col] is False:
            self.row -= 1
        elif direction == 'down' and self.row < self.rows - 1 and self.scene[self.row + 1][self.col] is False:
            self.row += 1
        elif direction == 'left' and self.col > 0 and self.scene[self.row][self.col - 1] is False:
            self.col -= 1
        elif direction == 'right' and self.col < self.cols - 1 and self.scene[self.row][self.col + 1] is False:
            self.col += 1
        elif direction == 'up-left' and self.row > 0 and self.col > 0 and self.scene[self.row - 1][self.col - 1] is False:
            self.row -= 1
            self.col -= 1
        elif direction == 'up-right' and self.row > 0 and self.col < self.cols - 1 and self.scene[self.row - 1][self.col + 1] is False:
            self.row -= 1
            self.col += 1
        elif direction == 'down-left' and self.row < self.rows - 1 and self.col > 0 and self.scene[self.row + 1][self.col - 1] is False:
            self.row += 1
            self.col -= 1
        elif direction == 'down-right' and self.row < self.rows - 1 and self.col < self.cols - 1 and self.scene[self.row + 1][self.col + 1] is False:
            self.row += 1
            self.col += 1
        else:
            return False
        return True
    
    def is_solved(self):
        return (self.row, self.col) == self.goal
    
    def copy(self):
        return GridNavigation(self.scene, (self.row, self.col), self.goal)
    
    def successors(self):
        for move in ['up', 'down', 'left', 'right', 'up-left', 'up-right', 'down-left', 'down-right']:
            newBoard = self.copy()
            if newBoard.perform_move(move):
                yield (move, (newBoard.row, newBoard.col), newBoard)
    
    def heruistic(self):
        return math.sqrt((self.row - self.goal[0]) ** 2 + (self.col - self.goal[1]) ** 2)

    # Required
    def find_path_a_star(self):
        frontier = PriorityQueue()
        index = 0
        frontier.put((self.heruistic(), 0, index, [self.start], self))
        explored = set()
        while frontier:
            _, g, _, position, board = frontier.get() #index to help get rid out priority queue comparing problem, '<' not supported between instances of 'GridNavigation' and 'GridNavigation'
            if (board.row, board.col) in explored:
                continue
            explored.add((board.row, board.col))
            if board.is_solved():
                print(position)
                return position
            for move, pos, next in board.successors():
                if (next.row, next.col) not in explored:
                    index += 1
                    distance = g + 1
                    if move in ['up-left', 'up-right', 'down-left', 'down-right']:
                        distance = g + math.sqrt(2)
                    frontier.put((distance + next.heruistic(), distance, index, position + [pos], next))

def find_path(start, goal, scene):
    board = GridNavigation(scene, start, goal)
    
    return board.find_path_a_star()

# scene = [[False, False, False],
#           [False, True , False],
#          [False, False, False]]
# find_path((0, 0), (2, 1), scene)

############################################################
# Section 3: Linear Disk Movement, Revisited
############################################################
def successors(A):
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

def heruistic(A):
    return sum([abs(i - val) for i, val in enumerate(A) if val >= 0])

def solve(A):        
    q = PriorityQueue()
    res = A[::-1]
    res = tuple(res)
    index = 0
    q.put((heruistic(A), 0, index, [], A))
    explored = set()
    while q:
        _, g, _, position, state = q.get()
        tupState = tuple(state)
        if tupState in explored:
            continue
        explored.add(tupState)
        if state == res:
            print(position)
            return position
        for move, newState in successors(state):
            if newState not in explored:
                index += 1
                distance = g + 1
                q.put((distance + heruistic(newState), distance, index, position + [move], newState))

def solve_distinct_disks(length, n):
    init = [i if i < n else -1 for i in range(length) ]
    return solve(init)

############################################################
# Section 4: Feedback
############################################################

# Just an approximation is fine.
feedback_question_1 = """ 8 hours to 10 hours"""

feedback_question_2 = """
should have know somthing about python PriorityQueue. Stuck there for 3 hours about object cant compare to object
"""

feedback_question_3 = """
I like 521. feels learnt a lot. A search is cool.
"""
