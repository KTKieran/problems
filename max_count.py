nums = [1, 3, 5, 1, -3, 9, 7, 9]  # 2 ( 9 is largest, occured twice)

def get_max_count(my_list):
    """
    count occurance of maximum number in the list

    Parameters
    ----------
    my_list: list

    Returns
    -------
    int: occurance of max number in the list

    """

    count_num =  0
    for n in my_list:
        largest_num = max(my_list)
        if n == largest_num:
            count_num = count_num + 1
    return count_num

print (get_max_count(nums))