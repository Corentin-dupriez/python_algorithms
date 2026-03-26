from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if len(nums) == 0:
            return
        mid = len(nums) // 2
        visited = TreeNode(nums[mid])
        left = nums[:mid]
        visited.left = self.sortedArrayToBST(left)
        right = nums[mid + 1:]
        visited.right = self.sortedArrayToBST(right)
        return visited


print(Solution().sortedArrayToBST([-10, -3, 0, 5, 9]).left.val)
        
