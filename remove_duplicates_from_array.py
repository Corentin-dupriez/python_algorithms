from collections import defaultdict
from typing import List


class Solution:
    def removeDuplicates(self, digits: List[int]) -> int:
        global nums
        numbers = defaultdict(int)

        for num in digits:
            numbers[num] = numbers.setdefault(num, 0) + 1

        nums = [x for x in numbers.keys()]

        return len([x for x in numbers.values()])


nums = [1, 1, 2]
print(Solution().removeDuplicates(nums))
print(nums)
