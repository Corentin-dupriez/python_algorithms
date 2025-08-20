def merge_arrays(left: list, right: list):
    length = len(left) + len(right)
    left_idx = 0
    right_idx = 0
    list_idx = 0

    new_list = [None] * length

    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] < right[right_idx]:
            new_list[list_idx] = left[left_idx]
            left_idx += 1
        else:
            new_list[list_idx] = right[right_idx]
            right_idx += 1
        list_idx += 1

    while left_idx < len(left):
        new_list[list_idx] = left[left_idx]
        left_idx += 1
        list_idx += 1

    while right_idx < len(right):
        new_list[list_idx] = right[right_idx]
        right_idx += 1
        list_idx += 1

    return new_list


def merge_sort(nums: list):
    if len(nums) == 1:
        return nums

    mid_idx = len(nums) // 2
    left = nums[:mid_idx]
    right = nums[mid_idx:]

    return merge_arrays(merge_sort(left), merge_sort(right))


digits = [int(x) for x in input().split()]

digits = merge_sort(digits)

print(*digits, sep=" ")
