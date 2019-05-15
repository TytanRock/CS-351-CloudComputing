#CS351 -- HW1
#Cory Ness

def greatest_difference(nums1, nums2):
    """ (list of number, list of number) -> number
    
    Return the greatest absolute difference between numbers at corresponding
    positions in nums1 and nums2.
    
    Precondition: len(nums1) == len(nums2) and nums1 != []
    
    # # >>> greatest_difference([1, 2, 3], [6, 8, 10])
    7
    >>> greatest_difference([1, -2, 3], [-6, 8, 10])
    # # 10
    # """
    if len(nums1) != len(nums2) or nums1 == []:
        print("Invalid Input\n")
        return 0

    greatest = 0
    for i in range(0, len(nums1)):
        if nums1[i] - nums2[i] > greatest:
            greatest = nums1[i] - nums2[i]
        if nums2[i] - nums1[i] > greatest:
            greatest = nums2[i] - nums1[i]
    
    print ("Greatest value is: ", greatest)
    return greatest

def can_pay_with_two_coins(denoms, amount):
    """ (list of int, int) -> bool
    
    Return True if and only if it is possible to form amount, which is a 
    number of cents, using exactly two coins, which can be of any of the 
    denominatins in denoms.
    
    >>> can_pay_with_two_coins([1, 5, 10, 25], 35)
    True
    >>> can_pay_with_two_coins([1, 5, 10, 25], 20)
    True
    >>> can_pay_with_two_coins([1, 5, 10, 25], 12)
    False
    """
    for i in range(0, len(denoms)):
        for j in range(i, len(denoms)):
            if denoms[i] + denoms[j] == amount:
                print("Found it!")
                print(denoms[i], " + ", denoms[j], " = ", amount)
                return True
    print("Could not find a combo")
    return False
	
def all_fluffy(s):
    """ (str) -> bool

    Return True iff every letter in s is fluffy. Fluffy letters are those that
    appear in the word 'fluffy'.
    
    >>> all_fluffy('fullfly')
    True
    >>> all_fluffy('firefly')
    False
    """
    fluffy_chars = ['f','l','u','y']
    for c in s:
        if not c in fluffy_chars:
            print("Not fluffy")
            return False
    print("Fluffy")
    return True

def digital_sum(nums_list):
    """ (list of str) -> int
    
    Precondition: s.isdigit() holds for each string s in nums_list.
    
    Return the sum of all the digits in all strings in nums_list.
    
    >>> digital_sum(['64', '128', '256'])
    34
    >>> digital_sum(['12', '3'])
    6
    """
    for s in nums_list:
        if not s.isdigit():
            print("Invalid input")
            return -1

    sum = 0
    for s in nums_list:
        for c in s:
            sum += int(c)
    print("Total is: ", sum)
    return sum


def count_collatz_steps(n):
    """ (int) -> int
    
    Return the number of steps it takes to reach 1, by applying the two steps
    of the Collatz conjecture beginning from n.

    >>> count_collatz_steps(6)
    8
    """
    count = 0
    while not n == 1:
        if n % 2 == 0:
            n = n / 2
            count += 1
        else:
            n = (n * 3) + 1
            count += 1
    print("Total is: ", count)
    return count
    
