# numbers = ['0','1','2','3','4']

ones_and_zeros = [1, 0, 0, 0, 1, 1]

zero_count = 0

for item in ones_and_zeros:
    print(item)
    if item == 0:
        zero_count = zero_count + 1

print(f'zero count = {zero_count}')

