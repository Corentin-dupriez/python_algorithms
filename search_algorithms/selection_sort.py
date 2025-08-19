digits = [int(x) for x in input().split()]

for idx in range(len(digits)):
    min_idx = idx
    for next_idx in range(idx + 1, len(digits)):
        if digits[next_idx] < digits[min_idx]:
            min_idx = next_idx
    digits[min_idx], digits[idx] = digits[idx], digits[min_idx]

print(*digits, sep=" ")
