############################################################
# CIS 521: Informed Search Homework
############################################################

from queue import PriorityQueue

student_name = "Type your full name here."

############################################################
# Imports
############################################################

# Include your imports here, if any are used.
import random
import heapq


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




                     


                    
            

TP = create_tile_puzzle(3, 3)
TP.perform_move('up')
TP.perform_move('down')
TP.perform_move('left')
TP.perform_move('right')






############################################################
# Section 2: Grid Navigation
############################################################

def find_path(start, goal, scene):
    pass

############################################################
# Section 3: Linear Disk Movement, Revisited
############################################################

def solve_distinct_disks(length, n):
    pass

############################################################
# Section 4: Feedback
############################################################

# Just an approximation is fine.
feedback_question_1 = 0

feedback_question_2 = """
Type your response here.
Your response may span multiple lines.
Do not include these instructions in your response.
"""

feedback_question_3 = """
Type your response here.
Your response may span multiple lines.
Do not include these instructions in your response.
"""
