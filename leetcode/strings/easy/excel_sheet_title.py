from collections import deque

class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        sol = deque()
        while columnNumber > 0:
            columnNumber -= 1

            sol.appendleft(chr(columnNumber % 26 + 65))
            columnNumber //= 26


        return ''.join(sol)

print(Solution().convertToTitle(1))
print(Solution().convertToTitle(28))
print(Solution().convertToTitle(701))
