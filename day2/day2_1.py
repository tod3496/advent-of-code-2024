DATAFILE = 'day2.data'
REPORTS = []

with open(DATAFILE) as f:
    for line in f:
        REPORTS.append([int(ele) for ele in line.split()])


def is_ascending(a, b):
    return a < b


def safe_diff(a, b):
    diff = abs(a - b)
    return 1 <= diff <= 3


def determine_safe(a_list):
    if len(a_list) <= 1:
        return True
    ascending = is_ascending(a_list[0], a_list[1])

    for i in range(1, len(a_list)):
        if is_ascending(a_list[i-1], a_list[i]) != ascending: 
            return False
        if not safe_diff(a_list[i-1], a_list[i]):
            return False
    
    return True


def main():
    safe_count = 0
    for report in REPORTS:
        if determine_safe(report):
            safe_count += 1
    print(safe_count)


if __name__ == '__main__':
    main()
