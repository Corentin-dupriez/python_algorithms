from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = 0
        j = 0
        k = 0

        temp_nums1 = nums1.copy()

        if n == 0:
            return
        

        while k < m + n:
            if j == n or temp_nums1[i] < nums2[j] and i < m and m != 0:
                nums1[k] = temp_nums1[i]
                i += 1
            else:
                nums1[k] = nums2[j]
                j += 1
            k += 1


nums1 = [2,0]
Solution().merge(nums1, 1, [1], 1)
print(nums1)

nums2 = [1]
Solution().merge(nums1, 1, [], 0)
print(nums2)

nums3 = [0]
Solution().merge(nums3, 0, [1], 1)
print(nums3)
