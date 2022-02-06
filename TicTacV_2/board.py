from move import Move
from player import Player


class Board:

    EMPTY_CELL = 0

    def __init__(self):
        self.game_board = [
                            [0, 0, 0],
                            [0, 0, 0],
                            [0, 0, 0]
                          ]

    def print_board(self):
        print("\n Position: ")
        self.print_board_with_positions()

        print("Board : ")
        for row in self.game_board :
            print(" |", end = "")
            for column in row:
                if column == Board.EMPTY_CELL:
                    print("   |", end = "")
                else:
                    print(f"{column}  |", end = "")
            print()

    def print_board_with_positions(self):
        print(" | 1 | 2 | 3 | \n | 4 | 5 | 6 | \n | 7 | 8 | 9 |")

    def submit_move(self, player, move):
        row = move.get_row()
        col = move.get_column()
        value = self.game_board[row][col]

        if value == Board.EMPTY_CELL:
            self.game_board[row][col] = player.marker
        else:
            print("This position already taken, Please choose the other one")

    def is_game_over(self, player, last_move):
        return ((self.check_row(player, last_move))
                or (self.check_col(player, last_move))
                or (self.check_diagonal(player))
                or (self.check_antigonal(player)))

    def check_row(self, player, last_move):
        row_index = last_move.get_row()
        board_row = self.game_board[row_index]

        return board_row.count(player.marker) == 3

    def check_col(self, player, last_move):
        marker_count = 0
        column_index = last_move.get_column()

        for i in range(3):
            if self.game_board[i][column_index] == player.marker:
                marker_count += 1
        return marker_count == 3

board = Board()
player = Player()
move = Move(5)


board.print_board()
board.submit_move(player, move)
board.print_board()
