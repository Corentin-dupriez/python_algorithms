from typing import DefaultDict, List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complements = DefaultDict()
        for i in range(len(nums)):
            if complements.get(nums[i]) is None:
                complements[target - nums[i]] = i
            else:
                return [complements[nums[i]], i]
        return []


print(Solution().twoSum(nums=[2, 7, 11, 15], target=9))
