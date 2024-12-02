from day2_1 import *


def remove_one(a_list):
    lists = []
    for i in range(len(a_list)):
        copy = a_list[:]
        copy.pop(i)
        lists.append(copy)
    return lists


def main():
    safe_count = 0
    for report in REPORTS:
        for one_removed in remove_one(report):
            if determine_safe(one_removed):
                print(True)
                safe_count += 1
                break
        else:
            print(False)
    print(safe_count)


if __name__ == '__main__':
    main()