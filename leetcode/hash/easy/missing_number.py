from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        return sum([n for n in range(len(nums)+1)]) - sum(nums)

print(Solution().missingNumber([3,0,1]))
print(Solution().missingNumber([0,1]))
print(Solution().missingNumber([9,6,4,2,3,5,7,0,1]))
