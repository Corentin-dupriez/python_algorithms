class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        solutions = []
        nums.sort()
        for i in range(len(nums)):
            if i != 0 and nums[i] == nums[i-1]: 
                continue
            a = nums[i]
            l = i + 1
            r = len(nums) - 1
            while l < r:
                total = a + nums[l] + nums[r]
                if total == 0:
                    if [a, nums[l], nums[r]] not in solutions:
                        solutions.append([a, nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                elif total < 0:
                    l += 1
                else:
                    r -= 1
        return solutions

print(Solution().threeSum([-1,0,1,2,-1,-4]))
print(Solution().threeSum([1,1,1]))
