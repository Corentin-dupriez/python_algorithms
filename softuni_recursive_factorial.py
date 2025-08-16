from calculate_time import calculate_time


@calculate_time
def calculate_factorial(n):
    if n == 0:
        return 1
    return n * calculate_factorial(n - 1)


print(f'Recursive factorial: {calculate_factorial(5)}')