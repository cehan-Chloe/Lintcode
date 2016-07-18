"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
class Solution:
    """
    @param root: The root of binary tree.
    @return: True if this Binary tree is Balanced, or false.
    """
    def maxDepth(self, root):
        if root is None:
            return 0
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        # at first, the abs is ignored and the operations when the maxdepth is calculated is wrong
        if left == -1 or right == -1 or abs(left - right) > 1:
            return -1
        return max(left, right) + 1
        
    def isBalanced(self, root):
        if root is None:
            return True
        return self.maxDepth(root) != -1
