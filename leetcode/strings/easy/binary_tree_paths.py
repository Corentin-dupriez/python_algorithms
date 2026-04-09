from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        res = []

        def dfs(path_string: str, node: Optional[TreeNode]): 
            if node is None: 
                return 
            if not node.left and not node.right:
                res.append(path_string+str(node.val))

            dfs(path_string+str(node.val) + "->", node.left)
            dfs(path_string+str(node.val) + "->", node.right)

        dfs("", root)
        return res



el1 = TreeNode(1)
el2 = TreeNode(2)
el3 = TreeNode(3)
el1.left = el2
el1.right = el3
el5 = TreeNode(5)
el2.right = el5

print(Solution().binaryTreePaths(el1))
