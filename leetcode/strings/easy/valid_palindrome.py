class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1
        while l < r: 
            if s[l].lower() == s[r].lower(): 
                l += 1
                r -= 1
            elif (not s[l].isalpha() and not s[l].isnumeric()) or s[l] == ' ':
                l += 1
            elif (not s[r].isalpha() and not s[r].isnumeric()) or s[r] == ' ':
                r -=1 
            else: 
                return False
        return True

print(Solution().isPalindrome("A man, a plan, a canal: Panama"))
print(Solution().isPalindrome("race a car"))
print(Solution().isPalindrome("P0"))