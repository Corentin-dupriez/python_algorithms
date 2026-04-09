class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        res = 0
        for i in range(len(columnTitle)): 
            res = res  * 26 + ord(columnTitle[i]) - 64 
        return res

print('A')
print(Solution().titleToNumber("A"))
print('--------')
print('AB')
print(Solution().titleToNumber("AB"))
print('--------')
print('ZY')
print(Solution().titleToNumber("ZY"))
print('--------')
