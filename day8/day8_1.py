import sys

try:
    DATAFILE = sys.argv[1]
except IndexError:
    print('usage: python3 day8_X.py <DATAFILE>')
    quit()

NODES = {}
try:
    with open(DATAFILE) as f:
        lines = f.readlines()
        HEIGHT = len(lines)
        WIDTH = len(lines[0].strip())
        for row, line in enumerate(lines):
            for col, freq in enumerate(line.strip()):
                if freq == '.':
                    continue
                if freq not in NODES.keys():
                    NODES[freq] = [(row, col)]
                else: 
                    NODES[freq].append((row, col))
except FileNotFoundError:
    print('Error: that datafile doesn\'t exist!')
    quit()


def gen_anti_pair(a, b):
    '''
    given two coordinates, returns the two antinodes that they would generate
    '''
    dr = b[0] - a[0]
    dc = b[1] - a[1]

    anti_1 = (a[0] - dr, a[1] - dc)
    anti_2 = (b[0] + dr, b[1] + dc)

    return anti_1, anti_2


def validate_anti(coord):
    r = coord[0]
    c = coord[1]

    return 0 <= r < HEIGHT and 0 <= c < WIDTH


def gen_freq_antinodes(coords, antis: set):
    '''
    adds all valid coords of all antinodes for given list of coords
    to the set passed in by the parameter antis
    coords are expected to be of all the same freq
    '''
    for i in range(len(coords)):
        for j in range(i+1, len(coords)):
            possible_antis = gen_anti_pair(coords[i], coords[j])
            for anti in possible_antis:
                if validate_anti(anti):
                    antis.add(anti)
    

def main():
    antis = set()
    for freq in NODES:
        gen_freq_antinodes(NODES[freq], antis)
    print(len(antis))


if __name__ == '__main__':
    main()
