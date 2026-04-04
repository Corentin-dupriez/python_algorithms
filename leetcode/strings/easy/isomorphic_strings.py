class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        letters = {}
        for i in range(len(s)):
            if not letters.get(s[i]):
                if t[i] not in [letter for letter in letters.values()]:
                    letters[s[i]] = t[i]
                else:
                    return False
            else:
                if letters[s[i]] != t[i]:
                    return False
        return True


print(Solution().isIsomorphic("badc", "baba"))
print(Solution().isIsomorphic("f11", "b23"))
print(Solution().isIsomorphic("paper", "title"))
print(Solution().isIsomorphic("egg", "add"))
