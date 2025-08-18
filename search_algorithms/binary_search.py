def binary_search(elements: list, target: int):
    left = 0
    right = len(elements) - 1
    while left <= right:
        mid = (left + right) // 2

        if elements[mid] == target:
            return mid

        if target < elements[mid]:
            right = mid - 1

        if target > elements[mid]:
            left = mid + 1

    return -1


nums = [int(x) for x in input().split()]
target = int(input())

print(binary_search(nums, target))
