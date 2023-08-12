import time
from k_tictactoe import HumanPlayer, RandomComputerPlayer


class TicTacToe:
    def __init__(self):
        # we will use a single list to rep 3x3 board
        self.board = [' ' for _ in range(9)]
        self.current_winner = None  # keeps track of the winner

    def print_board(self):
        # this is just getting the rows
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')

    @staticmethod
    def print_board_nums():
        # 0 | 1 | 2 (tells us what number corresponds to what box)
        number_board = [[str(i) for i in range(j*3, (j+1)*3)]
                        for j in range(3)]
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')

    def available_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == ' ']
        # moves = []
        # for (i, spot) in enumerate(self.board):
        #     # ['x', 'x', 'o'] --> [(0, 'x'), (1, 'x'), (2, 'o')]
        #     if spot == ' ':
        #         moves.append(i)
        # return moves

    def empty_squares(self):
        return ' ' in self.board

    def num_empty_squares(self):
        return self.board.count()
        # return len(self.available_moves())

    def make_move(self, square, letter):
        # if a valid move, then make the move (assign square to letter)
        # then return true. if invalid, return false
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False

    def winner(self, square, letter):
        # you're a winner if there's 3 in a row anywhere -- and all possibilities need to be checked
        # first, let's check the row
        row_ind = square // 3
        row = self.board[row_ind*3: (row_ind + 1) * 3]
        if all([spot == letter for spot in row]):
            return True

        # check the columns
        col_ind = square % 3
        column = [self.board[col_ind + i*3] for i in range(3)]
        if all([spot == letter for spot in column]):
            return True

        # check the diagonals
        # only if the square is an even number (0, 2, 4, 6, 8)
        # these are the only moves possible to win a diagonal
        if square % 2 == 0:
            diagonal1 = [self.board[i]
                         for i in [0, 4, 8]]  # left to right diagonal
            if all([spot == letter for spot in diagonal1]):
                return True
            diagonal2 = [self.board[i]
                         for i in [2, 4, 6]]  # right to left diagonal
            if all([spot == letter for spot in diagonal2]):
                return True

        # if all of the checks fail
        return False


def play(game, x_player, o_player, print_game=True):
    # returns the winner of the game (the letter of the winner) or None for a tie
    if print_game:
        game.print_board_nums()

    letter = 'X'  # starting letter
    # iterate while the game still has empty squares
    # -- no need to worry about a winning condition per se because the loop
    # will break when that happens
    while game.empty_squares():
        # get the move from the appropriate player
        if letter == 'O':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)

        # define a function to make a move. . .
        if game.make_move(square, letter):
            if print_game:
                print(letter + f" makes a move to square {square}")
                game.print_board()
                print('')  # just an empty line for aesthetics

            if game.current_winner:
                if print_game:
                    print(letter + ' wins!')
                return letter

            # after we make a move, we need to alternate lettters
            letter = 'O' if letter == 'X' else 'X'  # switches the players
            # if letter == 'X':
            #     letter = 'O'
            # else:
            #     letter = 'X'

        # tiny break so things are easier to read
        time.sleep(0.8)

    if print_game:
        print("It's a tie!")


if __name__ == '__main__':
    x_player = HumanPlayer('X')
    o_player = RandomComputerPlayer('O')
    t = TicTacToe()
    play(t, x_player, o_player, print_game=True)
