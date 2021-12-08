import re
BOARD_SIZE = 5

def read_input(filename):
    with open(filename) as f:
        return [l.strip() for l in f.readlines() if l.strip() != '']

class Board:
    # rows = [] # store each row as array of hashes
    # columns = [] # store columns as array of hashes

    # marked_values = []
    # unmarked_values = []

    def __init__(self, board_matrix):
        self.rows = []
        self.columns = []

        self.marked_values = []
        self.unmarked_values = []

        for _, row in enumerate(board_matrix):
            self.rows.append(row)
            for col_index, col in enumerate(row):
                if len(self.columns) <= col_index:
                    self.columns.append([])
                self.columns[col_index].append(col)

                self.unmarked_values.append(col)

    def mark(self, draw_num):
        if draw_num in self.unmarked_values:
            self.unmarked_values = list(filter(lambda x: False if draw_num == x else True, self.unmarked_values))
            self.marked_values.append(draw_num)

            self.rows = [
                list(filter(lambda x: False if draw_num == x else True, row))
                for row in self.rows
            ]
            self.columns = [
                list(filter(lambda x: False if draw_num == x else True, column))
                for column in self.columns
            ]

    def iz_win(self):
        for row in self.rows:
            if len(row) == 0:
                return True
        for col in self.columns:
            if len(col) == 0:
                return True



def main():
    input = read_input('input.txt')

    draw = input[0].split(',')

    # initialize the game
    boards = []
    current_board_matrix = []
    for line in input[1:]:
        current_line = re.split('\s+', line)
        current_board_matrix.append(current_line)

        if len(current_board_matrix) == BOARD_SIZE:
            boards.append(Board(current_board_matrix))
            current_board_matrix = []


    for draw_num in draw:
        for board in boards:
            board.mark(draw_num)

            if board.iz_win():
                print('winning board is', board.rows)
                print('board.unmarked_values', board.unmarked_values)
                print('board.marked_values', board.marked_values)
                print('lmabda', sum(list(map(lambda x: int(x), board.unmarked_values))))
                print('drawnum', draw_num)
                print(sum(list(map(lambda x: int(x), board.unmarked_values))) * int(draw_num))
                return None

if __name__ == '__main__':
    main()
