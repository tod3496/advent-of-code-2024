import sys

try:
    filepath = sys.argv[1]
except IndexError:
    print('usage: python3 day9_X.py <filepath>')
    exit(1)

try:
    with open(filepath) as f:
        DATA = f.readline().strip()
except FileNotFoundError:
    print('provided filepath doesn\'t exist')
    exit(1)


def create_blocks(line):
    blocks = []
    for i in range(len(line)):
        if i % 2 == 0:
            # files
            blocks.extend([i//2 for _ in range(int(line[i]))])
        else:
            # free space
            blocks.extend(['.' for _ in range(int(line[i]))])
    return blocks


def move_file_blocks(blocks):
    l = 0
    r = len(blocks) - 1
    while l < r:
        if blocks[l] != '.':
            l += 1
            continue
        if blocks == '.':
            r -= 1
            continue

        blocks[l] = blocks[r]
        blocks[r] = '.'
        r -= 1


def calc_checksum(blocks):
    checksum = 0
    for i in range(len(blocks)):
        if blocks[i] == '.':
            break
        checksum += i * blocks[i]
    return checksum


def main():
    blocks = create_blocks(DATA)
    move_file_blocks(blocks)
    for block in blocks:
        print(block, end='')
    print()
    print(calc_checksum(blocks))


if __name__ == '__main__':
    main()
