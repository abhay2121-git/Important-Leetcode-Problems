# Example 1:
# Input: root = [3,9,20,null,null,15,7]
# Output: 24

# Example 2:
# Input: root = [1]
# Output: 0

from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        total = 0

        if root.left and not root.left.left and not root.left.right:
            total += root.left.val
        else:
            total += self.sumOfLeftLeaves(root.left)

        total += self.sumOfLeftLeaves(root.right)

        return total
    