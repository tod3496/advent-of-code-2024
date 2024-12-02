DATAFILE = 'day1.data'
LEFT_LIST = []
RIGHT_LIST = []


with open(DATAFILE) as f:
    for line in f:
        tokens = line.split()
        LEFT_LIST.append(int(tokens[0]))
        RIGHT_LIST.append(int(tokens[1]))


def total_distance(list_a, list_b):
    sum_dist = 0
    for i in range(len(list_a)):
        sum_dist += abs(list_a[i] - list_b[i])

    print(sum_dist)


def main():
    sorted_left = sorted(LEFT_LIST)
    sorted_right = sorted(RIGHT_LIST)

    print(total_distance(sorted_left, sorted_right))
    

if __name__ == '__main__':
    main()