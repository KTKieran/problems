

def fibonacci(N):
    """
    Gives the nth term in the fibonacci series

    Parameters
    ----------
    N: int

    Returns
    -------
    int : nth term in the fibonacci series
    """
    number1 = 0
    number2 = 1
    for _ in range(N):
        final_number = number1 + number2
        number1 = number2
        number2 = final_number
    return final_number

print(fibonacci(10))