from typing import List

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest = None
        for num in range(len(nums)):
            if num != 0 and nums[num] == nums[num-1]:
                continue
            a = nums[num]
            l = num + 1
            r = len(nums) - 1
            while l < r:
                res = a + nums[l] + nums[r]
                if res == target:
                    return res
                if not closest: 
                    closest = res
                    if closest < target: 
                        l += 1
                    else:
                        r -= 1
                else:
                    if abs(res - target) <= abs(closest - target):
                        closest = res
                    if res < target:
                        l += 1
                    else: 
                        r -= 1
        return closest



print(Solution().threeSumClosest([-1, 2, 1, -4], 1))

print(Solution().threeSumClosest([0, 0, 0], 1))
print(Solution().threeSumClosest([10,20,30,40,50,60,70,80,90], 1))
print(Solution().threeSumClosest([-4,2,2,3,3,3], 0))
print(Solution().threeSumClosest([2, 5, 6, 7], 16))
print(Solution().threeSumClosest([1,2,7,13], 12))
print(Solution().threeSumClosest([-1000,-5,-5,-5,-5,-5,-5,-1,-1,-1], -8))
