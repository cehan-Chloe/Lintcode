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
    @return: True if the binary tree is BST, or false
    """  
    # all of the elements from the left child
    def isValidBST(self, root):
        self.min = -sys.maxint - 1
        self.max = sys.maxint
        return self.isValid(root, self.min, self.max)
        
    def isValid(self, root, min, max):
        if root is None:
            return True
        if root.val <= min or root.val >= max:
            return False
        return self.isValid(root.left, min, root.val) and self.isValid(root.right, root.val, max)
