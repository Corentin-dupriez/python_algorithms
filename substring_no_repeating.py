from collections import defaultdict


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        visited_chars = defaultdict(int)
        start_pointer = 0
        max_length = 0

        for end_pointer in range(len(s)):
            if s[end_pointer] in visited_chars:
                start_pointer = max(start_pointer, visited_chars[s[end_pointer]] + 1)
            visited_chars[s[end_pointer]] = end_pointer
            max_length = max(max_length, end_pointer - start_pointer + 1)
        return max_length


print(Solution().lengthOfLongestSubstring("abcabcbb"))
print(Solution().lengthOfLongestSubstring("bbbbb"))
print(Solution().lengthOfLongestSubstring("pwwkew"))
