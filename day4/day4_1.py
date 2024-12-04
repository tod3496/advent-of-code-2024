import re

DATAFILE = 'day4.data'
UP = -1
DOWN = 1
LEFT = -1
RIGHT = 1

LINES = []
with open(DATAFILE) as f:
    for line in f:
        LINES.append(line.strip())


def get_line(lines: list[str], start_row, start_col, row_incr, col_incr):
    row = start_row
    col = start_col

    string = ''

    while 0 <= row < len(lines) and 0 <= col < len(lines[row]):
        string += lines[row][col]
        row += row_incr
        col += col_incr
    
    return string


def seperate_directions(lines):
    '''
    takes a 2d array of characters and returns all of the
    horizontals, verticals, and diagonals as strings
    '''
    horizontals = []
    for r in range(len(lines)):
        horizontals.append(get_line(lines, r, 0, 0, RIGHT))

    verticals = []
    for c in range(len(lines[0])):
        verticals.append(get_line(lines, 0, c, DOWN, 0))

    right_diagonals = []
    for r in range(len(LINES)):
        right_diagonals.append(get_line(LINES, r, 0, DOWN, RIGHT))
    for c in range(1, len(LINES[0])):
        right_diagonals.append(get_line(LINES, 0, c, DOWN, RIGHT))

    left_diagonals = []
    for r in range(len(LINES)):
        left_diagonals.append(get_line(LINES, r, len(LINES[r]) - 1, DOWN, LEFT))
    for c in range(0, len(LINES[0]) - 1):
        left_diagonals.append(get_line(LINES, 0, c, DOWN, LEFT))

    return horizontals, verticals, right_diagonals, left_diagonals


def search_string(string):
    count = 0
    count += len(re.findall('XMAS', string))
    count += len(re.findall('SAMX', string))
    return count


def main():
    count = 0

    for direction in seperate_directions(LINES):
        for string in direction:
            count += search_string(string)

    print(count)


if __name__ == '__main__':
    main()
    