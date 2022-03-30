num = 6
factorial = 1
for n in range(1, num + 1):
    factorial = factorial * n
    print(factorial)



def calculate_factorial(n: int) -> int:
    """ Function for calculation factorial depends on parameter. -----DocString

    :Parameters:
        - n int. for calculation factorial for specific n
    :Return:
        - int. factorial for value of n
    """
    if n == 1:
        return n
    return n * calculate_factorial(n - 1)


# 7 * factorial(6) * factorial(5) * factorial(4) * factorial(3) * factorial(2) * 1
print('----')
print(calculate_factorial(6))

'''
print('------')

for i in range(100, 1, -10):
    print('i = ', i)


l = [1, 2, 3, 4, 5]

print('reversed array: ', l[::-1])
'''