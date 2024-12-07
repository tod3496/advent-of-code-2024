import sys, time

try:
    DATAFILE = sys.argv[1]
except IndexError:
    print('usage: python3 day7_X.py <DATAFILE>')
    quit()

EQUATIONS = {}
try:
    with open(DATAFILE) as f:
        for line in f:
            test_value, nums = line.strip().split(':')
            EQUATIONS[int(test_value)] = [int(n) for n in nums.split()]
except FileNotFoundError:
    print('Error: that datafile doesn\'t exist!')
    quit()


def validate_equation(test_value, nums):
    '''
    backtracking solution:
    - base case is the len of ns is 1
    - first try + and recursively call
    - then try * and recursively call

    returns True if a + would result in solution
    returns True if a * would result in a solution
    returns False if there is no solution
    '''
    if len(nums) == 1:
        return test_value == nums[0] # test value = num is the goal
    
    # try +
    # test_value becomes test_value - nums[-1]
    if validate_equation(test_value - nums[-1], nums[:-1]):
        return True

    # try *
    # test_value becomes test_value / nums[-1] 
    if validate_equation(test_value / nums[-1], nums[:-1]):
        return True
    
    return False
    

def main():
    start = time.time()
    answer = 0

    for test_value in EQUATIONS:
        if validate_equation(test_value, EQUATIONS[test_value]):
            answer += test_value

    print(answer)
    print('time:', time.time() - start)


if __name__ == '__main__':
    main()
