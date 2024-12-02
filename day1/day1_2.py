from day1_1 import *


def similarity_score(list_a, list_b):
    counts = {}
    for element in list_b:
        if element in counts:
            counts[element] += 1
        else:
            counts[element] = 1
    
    total = 0
    for element in list_a:
        if element not in counts:
            continue
        total += counts[element] * element

    return total


def main():
    print(similarity_score(LEFT_LIST, RIGHT_LIST))


if __name__ == '__main__':
    main()