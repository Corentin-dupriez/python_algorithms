from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        res = 0
        l = 0
        r = len(nums) - 1

        while l <= r: 
            if nums[l] != val:
                res += 1
                l += 1
            else:
                nums[l], nums[r] = nums[r], nums[l]
                r -= 1

        return res

nums1 = [3,2,2,3]
print(Solution().removeElement(nums1, 3))
print(nums1)
nums2 = [0,1,2,2,3,0,4,2]
print(Solution().removeElement(nums2, 2))
print(nums2)