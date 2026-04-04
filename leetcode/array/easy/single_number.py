from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        visited = {}

        for num in nums:
            if not visited.get(num):
                visited[num] = 1
            else:
                visited[num] += 1

        return [num for num, count_num in visited.items() if count_num == 1][0]


print(Solution().singleNumber([2, 2, 1]))
print(Solution().singleNumber([4, 1, 2, 1, 2]))
print(Solution().singleNumber([1]))
