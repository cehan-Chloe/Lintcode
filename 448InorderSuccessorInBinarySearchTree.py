# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    """
    @param root <TreeNode>: The root of the BST.
    @param p <TreeNode>: You need find the successor node of p.
    @return <TreeNode>: Successor of p.
    """
    def inorderSuccessor(self, root, p):
        # contains some referece...
        if root is None or p is None:
            return None
        successor = None
        while root is not None and root.val != p.val:
            # the left tree
            if root.val > p.val:
                successor = root
                root = root.left
            # the right tree
            else:
                root = root.right
        # p.val > root.val but not in the BST
        if root is None:
            return None
        if root.right is None:
            return successor
        root = root.right
        while root.left is not None:
            root = root.left
        
        return root
                
                
        
