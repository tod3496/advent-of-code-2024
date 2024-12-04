from day4_1 import *


def cross_mas(lines, row, col):
    if lines[row][col] != 'A':
        return False
    
    top_left = lines[row-1][col-1]
    bottom_right = lines[row+1][col+1]
    top_right = lines[row-1][col+1]
    bottom_left = lines[row+1][col-1]

    if top_left not in 'MS' or \
        bottom_right not in 'MS' or \
        top_right not in 'MS' or \
        bottom_left not in 'MS':
            return False
    
    if top_left == bottom_right:
        return False
    if top_right == bottom_left:
        return False
    
    return True


def main():
    count = 0
    for r in range(1, len(LINES) - 1):
        for c in range(1, len(LINES[0]) - 1):
            if cross_mas(LINES, r, c):
                count += 1
    print(count)


if __name__ == '__main__':
    main()