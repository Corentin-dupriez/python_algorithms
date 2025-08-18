def find_all_solutions(idx, words_by_idx, words_count, path, target):
    if idx == len(target):
        print(" ".join(path))
        return
    if idx not in words_by_idx:
        return
    for word in words_by_idx[idx]:
        if words_count[word] == 0:
            continue

        path.append(word)
        words_count[word] -= 1

        find_all_solutions(idx + len(word), words_by_idx, words_count, path, target)

        path.pop()
        words_count[word] += 1


words = input().split(", ")
target = input()

words_by_index = {}
words_count = {}
for w in words:
    words_count[w] = words_count.get(w, 0) + 1

for word in words:
    start = 0
    while True:
        start = target.find(word, start)
        if start == -1:
            break

        words_by_index.setdefault(start, []).append(word)
        start += 1

find_all_solutions(0, words_by_index, words_count, [], target)

