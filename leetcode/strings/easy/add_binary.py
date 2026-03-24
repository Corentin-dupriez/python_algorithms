class Solution:
    def addBinary(self, a: str, b: str) -> str:
        decimal_a = int(a, 2)
        decimal_b = int(b, 2)

        decimal_sum = decimal_a + decimal_b

        return bin(decimal_sum)[2:]


print(Solution().addBinary('101', '11'))
