class Solution:
    def reverse(self, x: int) -> int:
        negative = x < 0
        digits = ""

        x = abs(x)
        x_list = list(str(x))

        for num in range(len(x_list) - 1, -1, -1):
            digits += str(x_list[num])

        digits = int(digits) if not negative else -int(digits)

        if not -(2**31) <= digits < 2**31 - 1:
            return 0

        return digits


print(Solution().reverse(123))
print(Solution().reverse(-123))
print(Solution().reverse(120))
