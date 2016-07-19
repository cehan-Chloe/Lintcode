"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
import copy
class Solution:
    """
    @param root: The root of the binary search tree.
    @param A and B: two nodes in a Binary.
    @return: Return the least common ancestor(LCA) of the two nodes.
    """ 
            
    def lowestCommonAncestor(self, root, A, B):
        # divide and conquer
        if root is None or root.val == A.val or root.val == B.val:
            return root
        left = self.lowestCommonAncestor(root.left, A, B)
        right = self.lowestCommonAncestor(root.right, A, B)
        
        if left != None and right != None:
            return root
        if left != None:
            return left
        if right != None:
            return right
        return None
            

