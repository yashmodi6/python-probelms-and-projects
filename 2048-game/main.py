import os
import random


class Game2048:
    def __init__(self):
        self.board = [[0] * 4 for _ in range(4)]
        self.score = 0
        self.spawn_tile()
        self.spawn_tile()

    def spawn_tile(self):
        # Places a new 2 (90% chance) or 4 (10% chance) in an empty cell
        empty_cells = [
            (r, c) for r in range(4) for c in range(4) if self.board[r][c] == 0
        ]
        if empty_cells:
            r, c = random.choice(empty_cells)
            self.board[r][c] = 2 if random.random() < 0.9 else 4

    def print_board(self):
        # Clears the console and renders the current game state.
        os.system("cls" if os.name == "nt" else "clear")
        print(f"--- 2048 GAME --- Score: {self.score}")
        print("-" * 25)
        for row in self.board:
            row_str = "|"
            for val in row:
                if val == 0:
                    row_str += "     |"
                else:
                    row_str += f"{val:^5}|"
            print(row_str)
            print("-" * 25)
        print("Controls: W (Up) | A (Left) | S (Down) | D (Right) | Q (Quit)")

    def _slide_left_row(self, row):
        # Compresses and merges a single row to the left.
        # Shift everything to the left (remove zeros)
        non_zeros = [val for val in row if val != 0]

        # Merge adjacent matching elements
        new_row = []
        skip = False
        for i in range(len(non_zeros)):
            if skip:
                skip = False
                continue
            if i + 1 < len(non_zeros) and non_zeros[i] == non_zeros[i + 1]:
                merged_val = non_zeros[i] * 2
                new_row.append(merged_val)
                self.score += merged_val
                skip = True
            else:
                new_row.append(non_zeros[i])

        # Pad with zeros until length is 4
        new_row += [0] * (4 - len(new_row))
        return new_row

    def move(self, direction):
        # Performs board transformations to handle movements in 4 directions.
        moved = False
        direction = direction.upper()

        if direction == "A":  # Left
            for i in range(4):
                new_row = self._slide_left_row(self.board[i])
                if new_row != self.board[i]:
                    moved = True
                self.board[i] = new_row

        elif direction == "D":  # Right
            for i in range(4):
                # Reverse row, slide left, reverse back
                reversed_row = self.board[i][::-1]
                new_row = self._slide_left_row(reversed_row)
                new_row = new_row[::-1]
                if new_row != self.board[i]:
                    moved = True
                self.board[i] = new_row

        elif direction == "W":  # Up
            for c in range(4):
                col = [self.board[r][c] for r in range(4)]
                new_col = self._slide_left_row(col)
                if new_col != col:
                    moved = True
                for r in range(4):
                    self.board[r][c] = new_col[r]

        elif direction == "S":  # Down
            for c in range(4):
                col = [self.board[r][c] for r in range(4)][::-1]
                new_col = self._slide_left_row(col)
                new_col = new_col[::-1]
                if new_col != [self.board[r][c] for r in range(4)]:
                    moved = True
                for r in range(4):
                    self.board[r][c] = new_col[r]

        if moved:
            self.spawn_tile()

        return moved

    def is_game_over(self):
        # Checks if the game has no valid moves left.
        for r in range(4):
            for c in range(4):
                if self.board[r][c] == 0:
                    return False
                if r + 1 < 4 and self.board[r][c] == self.board[r + 1][c]:
                    return False
                if c + 1 < 4 and self.board[r][c] == self.board[r][c + 1]:
                    return False
        return True

    def check_win(self):
        # Checks if the user reached the 2048 tile.
        for row in self.board:
            if 2048 in row:
                return True
        return False


def main():
    game = Game2048()
    won_message_shown = False

    while True:
        game.print_board()

        if game.check_win() and not won_message_shown:
            print("🎉 Congratulations! You reached 2048! 🎉")
            print("Press enter to continue playing, or Q to quit.")
            won_message_shown = True

        if game.is_game_over():
            print("☠️ Game Over! No more valid moves remaining.")
            break

        user_input = input("Enter your move: ").strip().upper()

        if user_input == "Q":
            print("Thanks for playing!")
            break

        if user_input in ["W", "A", "S", "D"]:
            game.move(user_input)
        else:
            print("Invalid key! Please use W, A, S, or D.")


if __name__ == "__main__":
    main()
