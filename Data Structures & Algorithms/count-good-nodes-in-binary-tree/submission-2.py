# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def count(root, mval):
            if not root:
                return 0
            
            valid = 0
            if root.val >= mval:
                valid = 1 
                mval = root.val
            return valid + count(root.left, mval) + count(root.right, mval)
        
        out = count(root, -101)
        return out
        