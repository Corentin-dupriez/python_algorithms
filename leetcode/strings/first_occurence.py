class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        def construct_lps(needle):
            lps = [0] * len(needle)
            len_ = 0
            i = 1

            while i < len(needle):
                if needle[i] == needle[len_]:
                    len_ += 1
                    lps[i] = len_
                    i += 1
                else:
                    if len_ != 0:
                        len_ = lps[len_ - 1]
                    else:
                        lps[i] = 0
                        i += 1
            return lps
        
        if len(needle) > len(haystack): 
            return -1

        lps = construct_lps(needle)

        i = 0
        j = 0
        while i < len(haystack):
            if haystack[i] == needle[j]: 
                i += 1
                j += 1
                if j == len(needle):
                    return i - j
            else: 
                if j != 0:
                    j = lps[j - 1]
                else:
                    i += 1
        return -1


print(Solution().strStr('sadbutsad', 'sad'))
print(Solution().strStr('leetcode', 'leeto'))
print(Solution().strStr('hello', 'll'))
print(Solution().strStr('aaaaa', 'bba'))
print(Solution().strStr('aaa', 'aa'))
print(Solution().strStr('aaa', 'aaaa'))
print(Solution().strStr('mississippi', 'issip'))
print(Solution().strStr('mississippi', 'issipi'))
print(Solution().strStr('mississippi', 'sipp'))
