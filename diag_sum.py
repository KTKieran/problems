arr = [[1, 2, 3, 4],
       [5, 6, 7, 8],
       [9, 10, 11, 12],
       [13, 14, 15, 16]]


def diag_sum(my_arr):
       sum = 0
       for n in range(len(my_arr)):
              for m in range(len(my_arr[n])):
                     if n == m:
                            sum =  sum + my_arr[n][m]

       return sum

def rev_diag_sum(my_arr):
       sum = 0
       for n in range (len(my_arr)):
              for m in range (len(my_arr[n])):
                     if n + m == len(my_arr) -1:
                            sum = sum + my_arr[n][m]
       return sum

def dia_sum_offset(my_arr, offset):
       sum = 0
       for n in range (len(my_arr)):
              for m in range (len(my_arr[n])):
                     if (n + 1) == (m + 1):
                            sum = sum + my_arr[n][m]
       return sum


print(diag_sum(arr))
print(rev_diag_sum(arr))
print(dia_sum_offset(arr, 2))
print(__file__)
