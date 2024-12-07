from day7_1 import *


def validate_equation_2(test_value, nums, running_total):
    '''
    backtracking solution:
    - base case is the len of ns is 0
    - first try + and recursively call
    - then try * and recursively call
    - then try || and recursively call

    returns True if a + would result in solution
    returns True if a * would result in a solution
    returns True if a || would result in a solution
    returns False if there is no solution
    '''
    if len(nums) == 0:
        return test_value == running_total
    
    # try +
    # running_total becomes running_total + nums[0]
    if validate_equation_2(test_value, nums[1:], running_total + nums[0]):
        return True

    # try *
    # running_total becomes running_total * nums[0] 
    if validate_equation_2(test_value, nums[1:], running_total * nums[0]):
        return True
    
    # try ||
    # running_total is concatenated with nums[0]
    concat = int(str(running_total) + str(nums[0]))
    if validate_equation_2(test_value, nums[1:], concat):
        return True
    
    return False


def main():
    start = time.time()
    answer = 0
    
    for test_value in EQUATIONS:
        first = EQUATIONS[test_value].pop(0)
        if validate_equation_2(test_value, EQUATIONS[test_value], first):
            answer += test_value

    print(answer)
    print('time:', time.time() - start)


if __name__ == '__main__':
    main()
