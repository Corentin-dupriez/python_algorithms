string = input().split()


def reverse_array(string: list, idx: int) -> None:
    if idx == len(string) - 1:
        print(string[idx], end=" ")
        return
    reverse_array(string, idx + 1)
    print(string[idx], end=" ")


reverse_array(string, 0)
