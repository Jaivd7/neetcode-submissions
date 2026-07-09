# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        left = self.levelOrder(root.left)
        right = self.levelOrder(root.right)
        r = max(len(left), len(right))
        out = [[root.val]]
        for i in range(r):
            if i<len(left) and i<len(right):
                combined = left[i] + right[i]
            elif i<len(left):
                combined = left[i]
            else:
                combined = right[i]
            out.append(combined)
        return out