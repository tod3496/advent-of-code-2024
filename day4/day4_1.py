DATAFILE = 'day4.data'
UP = -1
DOWN = 1
LEFT = -1
RIGHT = 1

LINES = []
with open(DATAFILE) as f:
    for line in f:
        LINES.append(line.strip())


def search_line(lines: list[str], start_row, start_col, row_incr, col_incr):
    row = start_row
    col = start_col

    working_string = ''
    count = 0

    while 0 <= row < len(lines) and 0 <= col < len(lines[row]):
        working_string += lines[row][col]
        if 'XMAS' in working_string:
            working_string = ''
            count += 1
        row += row_incr
        col += col_incr

    return count


def main():
    count = 0

    # left to right
    for r in range(len(LINES)):
        count += search_line(LINES, r, 0, 0, RIGHT)

    # right to left
    for r in range(len(LINES)):
        count += search_line(LINES, r, len(LINES[r]) - 1, 0, LEFT)

    # top to bottom
    for c in range(len(LINES[0])):
        count += search_line(LINES, 0, c, DOWN, 0)

    # bottom to top
    for c in range(len(LINES[0])):
        count += search_line(LINES, len(LINES) - 1, c, UP, 0)

    # diagonal top left to bottom right
    for r in range(len(LINES)):
        count += search_line(LINES, r, 0, DOWN, RIGHT)
    for c in range(1, len(LINES[0])):
        count += search_line(LINES, 0, c, DOWN, RIGHT)

    # diagonal bottom right to top left
    for r in range(len(LINES)):
        count += search_line(LINES, r, len(LINES[r]) - 1, UP, LEFT)
    for c in range(0, len(LINES[0]) - 1):
        count += search_line(LINES, len(LINES) - 1, c, UP, LEFT)

    # diagonal top right to bottom left
    for r in range(len(LINES)):
        count += search_line(LINES, r, len(LINES[r]) - 1, DOWN, LEFT)
    for c in range(0, len(LINES[0]) - 1):
        count += search_line(LINES, 0, c, DOWN, LEFT)

    # diagonal bottom left to top right
    for r in range(len(LINES)):
        count += search_line(LINES, r, 0, UP, RIGHT)
    for c in range(1, len(LINES[0])):
        count += search_line(LINES, len(LINES) - 1, c, UP, RIGHT)

    print(count)


if __name__ == '__main__':
    main()