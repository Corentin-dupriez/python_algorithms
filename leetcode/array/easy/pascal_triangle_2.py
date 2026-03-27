from typing import List

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        triangle = []
        for r in range(rowIndex + 1):
            if r == 0: 
                triangle.append([1])
            else:
                row = []
                for c in range(r + 1): 
                    if 0 <= c < len(triangle[r-1]):
                        left_num = triangle[r-1][c]
                    else:
                        left_num = 0
                    if 0 <= c -1 <= len(triangle[r-1]):
                        right_num = triangle[r-1][c-1]
                    else: 
                        right_num = 0
                    row.append(left_num + right_num)
                triangle.append(row)
        return triangle[rowIndex]

print(Solution().getRow(3))
print(Solution().getRow(0))
print(Solution().getRow(1))