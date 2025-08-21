class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 0:
            return ""
        if numRows == 1:
            return s
        buckets = ["" for _ in range(numRows)]

        direction = 1
        row = 0
        for char in s:
            buckets[row] += char
            if row == numRows - 1:
                direction = -1

            elif row == 0:
                direction = 1

            row += direction
        return "".join(buckets)


print(
    Solution().convert(
        """PAYPALISHIRING""",
        3,
    )
)


print(
    Solution().convert(
        """ADC""",
        1,
    )
)
