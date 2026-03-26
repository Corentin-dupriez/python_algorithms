from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []
        for r in range(0, numRows):
            row = []
            for c in range(r+1): 
                if r > 0:
                    if 0 <= c-1 < len(res[r-1]):
                        left_num = res[r-1][c-1] 
                    else: 
                        left_num = 0
                    if 0 <= c < len(res[r-1]):
                        right_num = res[r-1][c] 
                    else:
                        right_num = 0
                    row.append(left_num + right_num)
                else: 
                    row.append(1)
            res.append(row)
        return res
       

print(Solution().generate(5))
