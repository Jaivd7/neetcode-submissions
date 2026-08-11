# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        
        def r(root):
            if not root:
                return (0,0)
            
            left = r(root.left)
            right = r(root.right)
            
            # (if you include the root.val, if you don't include the root.val)
            # print(root.val, (root.val + left[1] + right[1], max(left[0], left[1]) + max(right[0], right[1])))
            return (root.val + left[1] + right[1], max(left[0], left[1]) + max(right[0], right[1]))

        return max(r(root))