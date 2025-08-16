from calculate_time import calculate_time

@calculate_time
def recursive_sum(array):
    if len(array) == 1:
        return array[0]
    else:
        return array[0] + recursive_sum(array[1:])

@calculate_time
def recursive_sum_two(array, idx):
    if idx == len(array) -1:
        return array[idx]
    return array[idx] + recursive_sum_two(array, idx + 1)


@calculate_time
def builtin_sum(array):
    return sum(array)


print(f'Recursion: {recursive_sum([1, 2, 3, 4])}')
print(f'Recursion Two: {recursive_sum_two([1, 2, 3, 4], 0)}')
print(f'Built-in: {builtin_sum([1, 2, 3, 4])}')
