class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letters = {}
        for char in s: 
            if not letters.get(char): 
                letters[char] = 1
            else: 
                letters[char] += 1
        for char in t: 
            if not letters.get(char):
                return False
            else: 
                letters[char] -= 1
        if any([letters_count for letters_count in letters.values() if letters_count > 0]):
            return False
        return True


print(Solution().isAnagram('anagram', 'nagaram'))
print(Solution().isAnagram('rat', 'car'))
