############################################################
# CIS 521: adversarial_search
############################################################

student_name = "Type your full name here."

############################################################
# Imports
############################################################

# Include your imports here, if any are used.

import collections
import copy
import itertools
import random
import math

############################################################
# Section 1: Dominoes Game
############################################################

def create_dominoes_game(rows, cols):  
    return DominoesGame([[False] * cols for r in range(rows)])

class DominoesGame(object):

    # Required
    def __init__(self, board):
        self.board = board
        self.rows = len(board)
        self.cols = len(board[0])

    def get_board(self):
        return self.board 

    def reset(self):
        self.board = [[False] * self.cols for r in range(self.rows)]

    def is_legal_move(self, row, col, vertical):
        if row < 0 or row >= self.rows or col < 0 or col >= self.cols:
            return False
        if vertical:
            if row + 1 >= self.rows or self.board[row][col] or self.board[row + 1][col]:
                return False
        else:
            if col + 1 >= self.cols or self.board[row][col] or self.board[row][col + 1]:
                return False


    def legal_moves(self, vertical):
        for row in range(self.rows):
            for col in range(self.cols):
                if self.is_legal_move(row, col, vertical):
                    yield (row, col)

    def perform_move(self, row, col, vertical):
        if vertical:
            self.board[row][col] = True
            self.board[row + 1][col] = True
        else:
            self.board[row][col] = True
            self.board[row][col + 1] = True
        

    def game_over(self, vertical):
        return any(self.legal_moves(vertical))

    def copy(self):
        return DominoesGame(copy.deepcopy(self.board))


    def successors(self, vertical):
        for row, col in self.legal_moves(vertical):
            copy = self.copy()
            copy.perform_move(row, col, vertical)
            yield (row, col), copy

    def get_random_move(self, vertical):
        legal_moves = list(self.legal_moves(vertical))
        return random.choice(legal_moves) if legal_moves else None

    def utility(self, state, vertical):
        return len(list(state.legal_moves(vertical))) - len(list(state.legal_moves(not vertical)))

    def alphabeta_search(self, vertical, limit):
        def max_value(state, alpha, beta, depth):
            if depth == limit or not state.game_over(vertical):
                return None, self.utility(state, vertical), 1
            v = -math.inf
            best_move = None
            for move, successor in state.successors(vertical):
                _, u, nodes = min_value(successor, alpha, beta, depth + 1)
                if u > v:
                    v = u
                    best_move = move
                if v >= beta:
                    return best_move, v, nodes + 1
                alpha = max(alpha, v)
        
        def min_value(state, alpha, beta, depth):
            if depth == limit or not state.game_over(vertical):
                return None, self.utility(state, vertical), 1
            v = math.inf
            best_move = None
            for move, successor in state.successors(vertical):
                _, u, nodes = max_value(successor, alpha, beta, depth + 1)
                if u < v:
                    v = u
                    best_move = move
                if v <= alpha:
                    return best_move, v, nodes + 1
                beta = min(beta, v)
            return best_move, v, nodes + 1
        

        best_move, value, nodes = max_value(self, -math.inf, math.inf, limit)
        return best_move, value, nodes



    # Required
    def get_best_move(self, vertical, limit):
        return self.alphabeta_search(vertical, limit)

############################################################
# Section 2: Feedback
############################################################
g = create_dominoes_game(3, 4)
g1 = g.copy()
g.perform_move(-1, 0, True)
print(g.get_board() == g1.get_board())

g = create_dominoes_game(4, 4)
g2 = g.copy()
print(g.get_board() == g2.get_board())

g.get_random_move(True)
g.get_random_move(False) 

b = [[False] * 3 for i in range(3)]
g = DominoesGame(b)
g.get_best_move(True, 1)

feedback_question_1 = """

Type your response here.
Your response may span multiple lines.
Do not include these instructions in your response.
"""

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
