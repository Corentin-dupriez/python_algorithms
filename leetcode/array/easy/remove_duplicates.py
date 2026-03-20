from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        uniques = 0
        for i in range(len(nums) - 1, -1, -1):
            if i == 0 or nums[i] != nums[i -1]:
                uniques += 1
            else: 
                nums.pop(i)
        return uniques

list1 = [1,1,2]
print(Solution().removeDuplicates(list1))
print(list1)
list2 = [0,0,1,1,1,2,2,3,3,4]
print(Solution().removeDuplicates(list2))
print(list2)
