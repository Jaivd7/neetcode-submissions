# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        val = root.val

        def dfs(root,val):
            if not root:
                return 0
            if root.val >= val:
                l = dfs(root.left, root.val)
                r = dfs(root.right, root.val)
                return l + r + 1
            else:
                l = dfs(root.left, val)
                r = dfs(root.right, val)
                return l + r
        
        l = dfs(root.left, val)
        r = dfs(root.right, val)
        return l+r+1
        