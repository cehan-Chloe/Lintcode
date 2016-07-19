"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        this.val = val
        this.left, this.right = None, None
"""
class Solution:
    """
    @param root the root of binary tree.
    @return an integer
    """
    def maxPathSum2(self, root):
        # at first minus numbers are ignored
        if root is None:
            # the way to show the minimum number!
            return -sys.maxint - 1
        left = self.maxPathSum2(root.left)
        right = self.maxPathSum2(root.right)
        
        return root.val + max(0, left, right)
