class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.rstrip()
        length = 0

        for char in s[::-1]:
            if char != ' ': 
                length += 1
            else: 
                return length
        return length



print(Solution().lengthOfLastWord('Hello World'))
print(Solution().lengthOfLastWord('   fly me   to   the moon  '))
print(Solution().lengthOfLastWord('luffy is still joyboy'))
print(Solution().lengthOfLastWord('a'))
print(Solution().lengthOfLastWord('    day'))
print(Solution().lengthOfLastWord('day'))
