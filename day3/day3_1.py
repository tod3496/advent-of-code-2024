import re

DATAFILE = 'day3.data'

DATA = []

with open(DATAFILE) as f:
    for line in f:
        DATA.append(line)


def get_mul_list(a_list):
    output = []
    for line in a_list:
        output += re.findall(r'mul\(\d{1,3},\d{1,3}\)', line)
    return output


def calculate_mul_list(mul_list):
    output = 0
    for mul in mul_list:
        two_numbers = re.findall(r'\d+', mul)
        output += int(two_numbers[0]) * int(two_numbers[1])
    return output


def main():
    print(calculate_mul_list(get_mul_list(DATA)))


if __name__ == '__main__':
    main()