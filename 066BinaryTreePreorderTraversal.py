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
    @return: Preorder in ArrayList which contains node values.
    """
    # use divide and conquer
    def preorderTraversal(self, root):
        result = []
        if root is None:
            return result
        
        left = self.preorderTraversal(root.left)
        right = self.preorderTraversal(root.right)

        result.append(root.val);
        result += left
        result += right
        return result
