
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
    @return: Postorder in ArrayList which contains node values.
    """
    def postorderTraversal(self, root):
        result = []
        if root is None:
            return result
        result = self.postorderTraversal(root.left) + self.postorderTraversal(root.right) + [root.val]
        return result
