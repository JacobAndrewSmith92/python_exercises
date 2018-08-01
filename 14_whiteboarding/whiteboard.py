# Fibonacci Series

def fibonacci(n):
    """[summary]

    Arguments:
        n {[int]} -- [Takes one argument that is added to a range list]

    Returns:
        [int] -- [prints each fibonacci sequence # on a new line]
    """
    a = 0
    b = 1
    for i in range(0, n):
        temp = a
        a = b
        b = temp + b
    return a

# Display the first 15 Fibonacci numbers.
for c in range(0, 50):
    print(fibonacci(c))
