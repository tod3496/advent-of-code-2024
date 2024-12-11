from day10_1 import *


def main():
    result = 0
    for trailhead in TRAILHEADS:
        result += len(calc_trailhead_score(MAP, trailhead))
    print(result)


if __name__ == '__main__':
    main()
