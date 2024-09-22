import subprocess


class Board:
    def __init__(self) -> None:
        self.board = [[" " for _ in range(3)] for _ in range(3)]

    def print_board(self):
        subprocess.run(["cmd", "/c", "cls"], check=True)

        print("--- TIC-TAC-TOE GAME ---")
        print("-" * 25)

        for i, row in enumerate(self.board):
            row_str = "|"
            for val in row:
                row_str += f"{val:^5}|"

            print(row_str)

            if i < 2:
                print("|-----|-----|-----|")

        print("-" * 25)

    def place(self, row, col, player):
        if self.board[row][col] != " ":
            return False

        self.board[row][col] = player
        return True

    def is_full(self):
        return all(cell != " " for row in self.board for cell in row)

    def has_won(self, player):
        # Rows
        for row in self.board:
            if all(cell == player for cell in row):
                return True

        # Columns
        for col in range(3):
            if all(self.board[row][col] == player for row in range(3)):
                return True

        # Diagonals
        if all(self.board[i][i] == player for i in range(3)):
            return True

        if all(self.board[i][2 - i] == player for i in range(3)):
            return True

        return False


class Game:
    def __init__(self):
        self.board = Board()
        self.current_player = "X"

    def switch_player(self):
        self.current_player = "O" if self.current_player == "X" else "X"

    def get_move(self):
        while True:
            try:
                move = input(
                    f"Player {self.current_player}, enter row and column respectively (ex:1 3): "
                )

                row, col = map(int, move.split())
                row -= 1
                col -= 1

                if row not in range(3) or col not in range(3):
                    print("Enter numbers between 1 and 3.")
                    continue

                if self.board.place(row, col, self.current_player):
                    return

                print("That position is already occupied.")

            except ValueError:
                print("Enter two numbers, for example: 1 2")

    def run(self):
        while True:
            self.board.print_board()

            self.get_move()

            if self.board.has_won(self.current_player):
                self.board.print_board()
                print(f"Player {self.current_player} wins!")
                break

            if self.board.is_full():
                self.board.print_board()
                print("It's a draw!")
                break

            self.switch_player()


game = Game()
game.run()
