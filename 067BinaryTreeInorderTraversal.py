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
    @return: Inorder in ArrayList which contains node values.
    """
    def inorderTraversal(self, root):
        result = []
        if root is None:
            return result
        result = self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)
        return result
        
