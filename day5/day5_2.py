from day5_1 import *


def sort_update(update: list, before_dict, after_dict):
    '''
    sort of insertion sort
    tests if a slice of the update is in order, if not then move the page at
    index i one to the left until it is in order
    '''
    for i in range(1, len(update)):
        j = i
        while j > 0 and not update_in_order(update[:j] + [update[i]] + 
                                            update[j:i], before_dict, after_dict):
            # swap update[i] to the left
            j -= 1
        update.insert(j, update.pop(i))


def main():
    '''
    put the out of order updates in order then get sum the middle page
    '''
    before_dict, after_dict = get_before_after_dicts(PAGE_ORDERING_RULES)
    answer = 0
    for update in UPDATES:
        if not update_in_order(update, before_dict, after_dict):
            sort_update(update, before_dict, after_dict)
            answer += update[len(update) // 2]

    print(answer)


if __name__ == '__main__':
    main()
