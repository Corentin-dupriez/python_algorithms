digits = [int(x) for x in input().split()]

sorted = False
already_sorted = 0


while not sorted:
    sorted = True
    for idx in range(1, len(digits) - already_sorted):
        if digits[idx] < digits[idx - 1]:
            digits[idx], digits[idx - 1] = digits[idx - 1], digits[idx]
            sorted = False
    already_sorted += 1

print(*digits, sep=" ")
