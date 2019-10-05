arr = ['a', 'b', 'c', 'd', 'e', 'f', 'c', 'g']

# function to remove 'c' from my_list and return a new list
def remove_c(my_list):
    idx_pop = []
    for idx, val in enumerate (my_list):
        if 'c' == val:
            idx_pop.append(idx)

    for idx in idx_pop[::-1]:
        my_list.pop(idx)

    return (my_list)



if __name__ == "__main__":
    print(remove_c(arr))