from typing import List
from collections import defaultdict

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        visited = defaultdict(int)
        for i in range(len(nums)):
            current = visited.get(nums[i])
            if current is None: 
                visited[nums[i]] = i
            else:
                if i - current <= k:
                    return True
                else: 
                    visited[nums[i]] = i
        return False

print(Solution().containsNearbyDuplicate([1,2,3,1], 3))
print(Solution().containsNearbyDuplicate([1,0,1,1], 1))
print(Solution().containsNearbyDuplicate([1,2,3,1,2,3], 2))
