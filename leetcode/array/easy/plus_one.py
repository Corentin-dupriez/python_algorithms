from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1 
        for i in range(len(digits) - 1, -1, -1): 
            digits[i] += carry
            carry = 0
            if digits[i] >= 10:
                if i != 0:
                    digits[i] = 0
                    carry = 1
                else:
                    digits[0] = 0
                    temp_digits = digits
                    digits = list([1])
                    digits.extend(temp_digits)
        return digits

print(Solution().plusOne([1,2,3]))
print(Solution().plusOne([4,3,2,1]))
print(Solution().plusOne([9]))
