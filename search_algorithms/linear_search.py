nums = [1, 2, 3, 4, 5, 6, 7]
target = 5


def linear_search(nums, target):
    for idx, num in enumerate(nums):
        if num == target:
            return idx
    return -1


print(linear_search(nums, target))
