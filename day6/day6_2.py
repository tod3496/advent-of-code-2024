from day6_1 import *


def check_hypothetical_loop(map, start_row, start_col, start_direction, b_row, b_col):
    '''
    hypothetically, if there was a barrier at b_row, b_col, would you loop?
    '''
    location_directions = {}
    row = start_row
    col = start_col
    direction = start_direction

    while True:
        next_row = row + DIRECTIONS[direction][0]
        next_col = col + DIRECTIONS[direction][1]
        if next_row < 0 or next_row >= len(map) or next_col < 0 or \
                                        next_col >= len(map[0]):
            # goes off the edge = does not loop
            return False 
        if map[next_row][next_col] == '#' or (next_row == b_row and \
                                              next_col == b_col):
            direction = (direction + 1) % 4
        else:
            if (row, col) in location_directions.keys():
                if direction in location_directions[(row, col)]:
                    # already been in this location with this direction = loop
                    return True 
                location_directions[(row, col)].append(direction)
            else:
                location_directions[(row, col)] = [direction]
            row = next_row
            col = next_col
    

def main():
    start = time.time()
    count = 0
    positions = move_protocol(MAP, START_ROW, START_COL)
    positions.remove((START_ROW, START_COL))
    for (row,col) in positions:
        if check_hypothetical_loop(MAP, START_ROW, START_COL, 0, row, col):
            count += 1

    print(count)
    print('time:', time.time() - start)


if __name__ == '__main__':
    main()
