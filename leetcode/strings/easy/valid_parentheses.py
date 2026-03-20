class Solution:
    def isValid(self, s: str) -> bool:
        par = [] 
        for char in s: 
            if char in ('(', '[', '{'):
                par.append(char)
            else: 
                if (char == ')' and (len(par) == 0 or par.pop() != '(') 
                or char == ']' and (len(par) == 0 or par.pop() != '[')
                or char == '}' and (len(par) == 0 or par.pop() != '{')):
                    return False
        if len(par) == 0:
            return True
        return False

print(Solution().isValid('()'))
print(Solution().isValid('()[]{}'))
print(Solution().isValid('(]'))
print(Solution().isValid('([])'))
print(Solution().isValid('([)]'))
print(Solution().isValid('['))
print(Solution().isValid('(('))
print(Solution().isValid(']'))
