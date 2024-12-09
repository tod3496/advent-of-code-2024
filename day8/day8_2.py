from day8_1 import *


def gen_antis_2(a, b):
    '''
    given two coordinates, returns the two antinodes that they would generate
    '''
    dr = b[0] - a[0]
    dc = b[1] - a[1]

    antis = []
    
    r = a[0]
    c = a[1]
    while 0 <= r < HEIGHT and 0 <= c < WIDTH:
        antis.append((r, c))
        r = r - dr
        c = c - dc

    r = b[0]
    c = b[1]
    while 0 <= r < HEIGHT and 0 <= c < WIDTH:
        antis.append((r, c))
        r = r + dr
        c = c + dc

    return antis


def gen_freq_antinodes_2(coords, antis: set):
    '''
    adds all valid coords of all antinodes for given list of coords
    to the set passed in by the parameter antis
    coords are expected to be of all the same freq
    '''
    for i in range(len(coords)):
        for j in range(i+1, len(coords)):
            possible_antis = gen_antis_2(coords[i], coords[j])
            for anti in possible_antis:
                if validate_anti(anti):
                    antis.add(anti)


def main():
    antis = set()
    for freq in NODES:
        gen_freq_antinodes_2(NODES[freq], antis)
    print(len(antis))


if __name__ == '__main__':
    main()
