from day3_1 import *


def get_enabled(string: str):
    '''
    returns list of strings between do() and dont()
    '''
    return re.findall(r'do\(\).*don\'t\(\)', string)


def put_newlines_after_dont(string):
    return re.sub(r'don\'t\(\)', 'don\'t()\n', string)


def main():
    big_string = 'do()'
    for line in DATA:
        big_string += line.strip()
    big_string += 'don\'t()'

    # print(big_string)

    big_string2 = put_newlines_after_dont(big_string)
    # print(big_string2)

    enabled = get_enabled(big_string2)
    # print(enabled)

    mul_list = get_mul_list(enabled)
    # print(mul_list)

    print(calculate_mul_list(mul_list))


if __name__ == '__main__':
    main()