# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False


        def isEqual(root, subroot):
            if not root and not subroot:
                return True
            if not root or not subroot:
                return False
            if root.val == subroot.val:
                left = isEqual(root.left, subroot.left)
                right = isEqual(root.right, subroot.right)
                return left and right
            else:
                return False
        
        if isEqual(root, subRoot):
            return True
        else:
            return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)