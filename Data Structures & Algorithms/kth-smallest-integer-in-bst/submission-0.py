# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        out = []
        def inorder(root, out):
            if not root:
                return []
            l = inorder(root.left,out)
            l.append(root.val)
            r = inorder(root.right,out)
            return l+r
        kval = inorder(root,out)
        return kval[k-1]