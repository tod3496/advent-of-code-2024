DATAFILE = 'day6.data'

MAP = []
row = 0
with open(DATAFILE) as f:
    for line in f:
        MAP.append(line.strip())
        if '^' in line:
            START_COL = line.index('^')
            START_ROW = row
        row += 1

DIRECTIONS = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def move_protocol(map, start_row, start_col):
    '''
    Checks if the space after moving forward would be '#' then turn right,
    otherwise move forward
    Loops until the guard leaves the map
    Saves distinct locations in a set
    '''
    distinct_locations = set()
    direction = 0
    row = start_row
    col = start_col
    while True:
        next_row = row + DIRECTIONS[direction][0]
        next_col = col + DIRECTIONS[direction][1]
        if next_row < 0 or next_row >= len(map) or next_col < 0 or \
                next_col >= len(map[0]):
            distinct_locations.add((row, col))
            break
        if map[next_row][next_col] == '#':
            direction = (direction + 1) % 4
        else:
            distinct_locations.add((row, col))
            row = next_row
            col = next_col

    return distinct_locations


def main():
    positions = move_protocol(MAP, START_ROW, START_COL)
    print(len(positions))


if __name__ == '__main__':
    main()
