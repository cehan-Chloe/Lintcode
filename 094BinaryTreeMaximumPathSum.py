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
    @return: An integer
    """
    # let result to be a global variable
    def max(self, root, result):
        if root is None:
            return 0
        left = self.max(root.left, result)
        right = self.max(root.right, result)
        
        max_cur = max(left, 0) + max(right, 0) + root.val
        self.result = max(self.result, max_cur)
        # the root can only contain one subtree and the root node
        return max(left + root.val, right + root.val, root.val)
            
        
    def maxPathSum(self, root):
        if root is None:
            return 0
        self.result = root.val
        self.max(root, self.result)
        return self.result
