import sys
from collections import deque

try:
    filepath = sys.argv[1]
except IndexError:
    print('usage: python3 day10_X.py <filepath>')
    exit(1)

try:
    with open(filepath) as f:
        MAP = []
        TRAILHEADS = []
        for r, row in enumerate(f):
            row_lis = []
            for c, col in enumerate(row.strip()):
                icol = int(col)
                row_lis.append(icol)
                if icol == 0:
                    TRAILHEADS.append((r, c))
            MAP.append(row_lis)
except FileNotFoundError:
    print('filepath doesn\'t exist!')
    exit(1)


def calc_trailhead_score(map, trailhead):
    '''
    do bfs to find all possible paths to a 9
    '''
    frontier = deque()
    nines = []
    frontier.append((trailhead[0], trailhead[1], 0))

    directions = ((0, 1), (0, -1), (1, 0), (-1, 0))

    while len(frontier) > 0:
        row, col, height = frontier.popleft()

        for dr, dc in directions:
            new_row = row + dr
            new_col = col + dc

            if new_row < 0 or new_row >= len(map) or \
            new_col < 0 or new_col >= len(map[0]) or \
            map[new_row][new_col] != height + 1:
                continue
            if map[new_row][new_col] == 9:
                nines.append((new_row, new_col))
            else:
                frontier.append((new_row, new_col, height + 1))

    return nines



def main():
    result = 0
    for trailhead in TRAILHEADS:
        result += len(set(calc_trailhead_score(MAP, trailhead)))
    print(result)



if __name__ == '__main__':
    main()
