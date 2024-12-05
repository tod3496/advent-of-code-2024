DATAFILE = 'day5.data'

PAGE_ORDERING_RULES = []

UPDATES = []

with open(DATAFILE) as f:
    line = f.readline().strip()
    while line != '':
        PAGE_ORDERING_RULES.append([int(x) for x in line.split('|')])
        line = f.readline().strip()
    
    for line in f:
        UPDATES.append([int(x) for x in line.strip().split(',')])


def get_before_after_dicts(rules):
    '''
    before_dict: key = page number, value = all page numbers that are before it
    after_dict: same thing as before_dict except its pages after it
    '''
    before_dict = {}
    after_dict = {}

    for before, after in rules:
        if after in before_dict:
            before_dict[after].append(before)
        else:
            before_dict[after] = [before]
        
        if before in after_dict:
            after_dict[before].append(after)
        else:
            after_dict[before] = [after]

    return before_dict, after_dict


def update_in_order(update: list, before_dict: dict, after_dict: dict):
    '''
    check if the update is in the right order by checking if the nth element
    should come after all the elements to the left, and before all the elements
    to the right.
    '''
    for i in range(len(update)):
        for number in update[:i]: # all of the numbers to the left of i
            if update[i] in before_dict and number not in before_dict[update[i]]: 
                # number to the left of i is NOT before i
                return False
            
        for number in update[i+1:]: # all of the numbers to the right of i
            if update[i] in after_dict and number not in after_dict[update[i]]:
                # number to the right of i is NOT after i
                return False
            
    return True


def main():
    '''
    add up the middle pages of the correctly ordered updates
    '''
    before_dict, after_dict = get_before_after_dicts(PAGE_ORDERING_RULES)
    
    answer = 0
    for update in UPDATES:
        if update_in_order(update, before_dict, after_dict):
            answer += update[len(update) // 2]

    print(answer)


if __name__ == '__main__':
    main()
