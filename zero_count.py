"""
It calculates the largest amount of consecutive zeros in a list
"""

my_list = [0]*4 +[1]*2 +[0]*2 + [1]*2

def max_zero_calc(my_list):
    zero_count = 0
    max_zero = 0

    for num in my_list:
        if num == 0:
            zero_count = zero_count+1
        elif num == 1:
            zero_count = 0
        if zero_count > max_zero:
            max_zero = zero_count

    return max_zero

print(max_zero_calc(my_list))