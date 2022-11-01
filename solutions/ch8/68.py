'''
8.68 Write a program that can play Tic-Tac-Toe effectively. (See Section 5.6.)
To do this, you will need to create a game tree T, which is a tree where
each position corresponds to a game configuration, which, in this case,
is a representation of the Tic-Tac-Toe board. (See Section 8.4.2.) The
root corresponds to the initial configuration. For each internal position p
in T, the children of p correspond to the game states we can reach from
p's game state in a single legal move for the appropriate player, A (the
first player) or B (the second player). Positions at even depths correspond
to moves for A and positions at odd depths correspond to moves for B.
Leaves are either final game states or are at a depth beyond which we do
not want to explore. We score each leaf with a value that indicates how
good this state is for player A. In large games, like chess, we have to use a
heuristic scoring function, but for small games, like Tic-Tac-Toe, we can
construct the entire game tree and score leaves as +1, 0, -1, indicating
whether player A has a win, draw, or lose in that configuration. A good
algorithm for choosing moves is minimax. In this algorithm, we assign a
score to each internal position p in T, such that if p represents A's turn, we
compute p's score as the maximum of the scores of p's children (which
corresponds to A's optimal play from p). If an internal node p represents
B's turn, then we compute p's score as the minimum of the scores of p's
children (which corresponds to B's optimal play from p).
'''

from copy import deepcopy
from re import I
from LinkedTree import LinkedTree
from solutions.ch6.ArrayStack import ArrayStack

import random
from collections import namedtuple


Move = namedtuple('Move', 'player position')
Position = namedtuple('Position', 'row column')

class Board():
    def __init__(self, initial_state=None):
        self._state = initial_state if initial_state else [[None for i in range(3)] for j in range(3)]
        self._game_over = False
        self._is_draw = False
        self._last_move = None
        self._check_state()

    def __eq__(self, other):
        return type(other) is type(self) and \
            str(self._state) == str(other._state) and \
            self._game_over == other._game_over and \
            self._is_draw == other._is_draw and \
            self._last_move == other._last_move

    def __hash__(self):
        return hash((str(self._state), self._game_over, self._is_draw, self._last_move))

    def _validate(self, move):
        if not 0 <= move.position.row < 3 or \
            not 0 <= move.position.column < 3:
                raise ValueError('Invalid move!')

        if self._last_move != None and \
            self._last_move.player == move.player:
                raise ValueError('Invalid move!')

        if self._state[move.position.row][move.position.column] != None:
            raise ValueError('Invalid move!')

    def _check_state(self):
        # check rows
        for r in range(3):
            if self._state[r] == ['X', 'X', 'X'] or \
                self._state[r] == ['O', 'O', 'O']:
                self._game_over = True
                return

        # check columns
        for c in range(3):
            if [self._state[r][c] for r in range(3)] == ['X', 'X', 'X'] or \
                [self._state[r][c] for r in range(3)] == ['O', 'O', 'O']:
                self._game_over = True
                return

        # check diagonal
        if [self._state[i][i] for i in range(3)] == ['X', 'X', 'X'] or \
            [self._state[i][i] for i in range(3)] == ['O', 'O', 'O']:
                self._game_over = True
                return

        # check counter diagonal
        if [self._state[i][~i] for i in range(3)] == ['X', 'X', 'X'] or \
            [self._state[i][~i] for i in range(3)] == ['O', 'O', 'O']:
                self._game_over = True
                return

        # check if board is full
        for r in range(3):
            for c in range(3):
                if self._state[r][c] == None:
                    return

        # draw
        self._game_over = True
        self._is_draw = True 

    def get_legal_moves(self, player=None):
        moves = []
        for r in range(3):
            for c in range(3):
                if self._state[r][c] == None:
                    if player:
                        moves.append(Move(player, Position(r, c)))
                    else:
                        moves.append(Move('A', Position(r, c)))
                        moves.append(Move('B', Position(r, c)))
        return moves

    def get_score(self, player='A'):

        if not self.is_over():
            raise Exception('Game not over yet!')

        if self._is_draw:
            return 0

        if player == self._last_move.player:
            return 1
        else:
            return -1

    def is_over(self):
        return self._game_over

    def apply_move(self, move):
        if self.is_over():
            raise Exception('Game is over!')

        self._validate(move)
        self._state[move.position.row][move.position.column] = 'X' if move.player == 'A' else 'O'
        self._last_move = move

        self._check_state()

    def draw(self):    
        print(" %s | %s | %s " % (str(self._state[0][0] or ' '), str(self._state[0][1] or ' '), str(self._state[0][2] or ' ')))    
        print("___|___|___")    
        print(" %s | %s | %s " % (str(self._state[1][0] or ' '), str(self._state[1][1] or ' '), str(self._state[1][2] or ' ')))    
        print("___|___|___")    
        print(" %s | %s | %s " % (str(self._state[2][0] or ' '), str(self._state[2][1] or ' '), str(self._state[2][2] or ' ')))    
        print("   |   |   ")    
            
                  

class TicTacToe():

    def __init__(self, initial_state=None):
        if initial_state == None:
            initial_state = [[None for i in range(3)] for j in range(3)]
            initial_state[random.randint(0, 2)][random.randint(0, 2)] = 'X'  # A always starts first
        
        self.build_game_tree(initial_state)
        
        self._scores = {}
        self.compute_scores()

    def build_game_tree(self, initial_state=None):
        self._gameTree = LinkedTree(Board(initial_state))

        s = ArrayStack()
        s.push((self._gameTree.root(), 'B'))

        while not s.is_empty():
            p, next_player = s.pop()
            board = p.element()    
            
            if board.is_over():
                # we reached a leaf, nothing more to do
                pass
            else:
                if next_player == 'A':
                    legal_moves = board.get_legal_moves('A')
                else:
                    legal_moves = board.get_legal_moves('B')

                for move in legal_moves:
                    board_copy = deepcopy(board)  # first, make a clean copy of the board
                    board_copy.apply_move(move)
                    child = self._gameTree.add_child(p, board_copy)
                    if next_player == 'A':
                        s.push((child, 'B'))
                    else:
                        s.push((child, 'A'))

    def _compute_score(self, p, next_player):
        board = p.element()

        if p in self._scores:
            return self._scores[p]

        if self._gameTree.is_leaf(p):
            score = board.get_score()
            self._scores[p] = score
            return score
        else:
            if next_player == 'A':
                score = max(self._compute_score(child, 'B') for child in self._gameTree.children(p))
                self._scores[p] = score
                return score
            else:
                score = min(self._compute_score(child, 'A') for child in self._gameTree.children(p)) 
                self._scores[p] = score
                return score

    def compute_scores(self):
        self._compute_score(self._gameTree.root(), 'B')   
           
    def play_game(self):
        print("===== Python TicTacToe =====\n")
        print("Computer [X] --- Player [O]\n")  

        val = input("Start game? [y/n]: ")
        print('\n')
        
        if val == "y":
            p = self._gameTree.root()
            board = deepcopy(p.element())
            while not board.is_over():
                board.draw()

                row = int(input("Select row [0-2]: "))
                col = int(input("Select column [0-2]: "))
                print('======================\n')
                player_move = Move('B', Position(row, col))
                board.apply_move(player_move)

                if board.is_over():
                    break

                for q in self._gameTree.children(p):
                    if board == q.element():
                        max = -1
                        for r in self._gameTree.children(q):
                            if self._scores[r] > max:
                                max = self._scores[r]
                                board = deepcopy(r.element())
                                p = r

            board.draw()

            winner = None
            if board.get_score('A') == 1:
                winner = 'Computer'
            elif board.get_score('B') == 1:
                winner = 'Player'

            if winner:
                print('Game over. {} won!'.format(winner))
            else:
                print('Game over. Draw!')

            val = input('Play another one? [y/n]: ')
            if val == "y":
                self.play_game()

if __name__ == "__main__":
    initial_state = \
    [
        [None, None, None],
        [None, None, None],
        [None, None, None]
    ]

    initial_state = \
    [
        ['X', 'X', 'O'],
        [None, 'X', 'X'],
        [None, 'O', 'O']
    ]

    game = TicTacToe(None)
    game.play_game()