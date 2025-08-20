digits = [int(x) for x in input().split()]

for i in range(1, len(digits)):
    for j in range(i, 0, -1):
        if digits[j] < digits[j - 1]:
            digits[j], digits[j - 1] = digits[j - 1], digits[j]
        else:
            break

print(*digits, sep=" ")
