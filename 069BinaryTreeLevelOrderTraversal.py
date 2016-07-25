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
    @return: Level order in a list of lists of integers
    """
    def levelOrder(self, root):
        result = []
        if root is None:
            return result
        cur_level = [root]
        while cur_level:
            next_level = []
            # at first append i.left.val directly
            for i in cur_level:
                if i.left:
                    next_level.append(i.left)
                if i.right:
                    next_level.append(i.right)
            # at first the [] was ignored. every element in result is also a list
            result.append([cur.val for cur in cur_level])
            cur_level = next_level
        return result
