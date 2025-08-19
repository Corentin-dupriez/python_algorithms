def regression_binary_search(left: int, right: int, target: int):
    if not left <= right:
        return -1
    mid = (left + right) // 2
    if digits[mid] == target:
        return mid
    else:
        if target < digits[mid]:
            index = regression_binary_search(left, mid - 1, target)
        else:
            index = regression_binary_search(left + 1, mid, target)
    return index


digits = [int(x) for x in input().split()]
target = int(input())

print(regression_binary_search(0, len(digits) - 1, target))
