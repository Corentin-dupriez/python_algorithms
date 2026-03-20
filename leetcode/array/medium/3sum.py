class Solution:
    def two_sum(self, arr, target):
        s = set()
        for num in arr: 
            complement = target + num
            # print(f'Current target: {target}')
            # print(f'Current number: {num}')
            # print(f'Complement for number: {complement}')
            # print(f'Set: {s}')
            if complement in s:
                return [num, complement]
            s.add(num)

    def threeSum(self, nums: list[int]) -> list[list[int]]:
        solutions = {}
        nums.sort()
        for num in range(len(nums)):
            result = self.two_sum(nums[num:], nums[num])
            if result:
                solutions[nums[num + 1]] = result
        return solutions



print(Solution().threeSum([-1,0,1,2,-1,-4]))
#print(Solution().threeSum([-100,-70,-60,110,120,130,160]))
