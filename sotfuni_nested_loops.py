n = int(input())
word = [""] * n


def nested_loops(m: int, idx: int) -> None:
    if idx == n:
        print(*word, sep=" ")
        return
    for i in range(1, m + 1):
        word[idx] = str(i)
        nested_loops(m, idx + 1)


nested_loops(n, 0)
