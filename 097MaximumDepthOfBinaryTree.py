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
    def maxDepth(self, root):
        depth = 0
        if root is None:
            return depth
        depth = max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
        return depth
        
        
