# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # Use a que
        q = deque()

        if not root:
            return []
        
        q.append(root)
        res = []

        layer_count = 1
        while q:
            rightside = None
            new_lc = 0
            for i in range(layer_count):
                node = q.popleft()
                if node:
                    rightside = node
                    if node.left:
                        q.append(node.left)
                        new_lc += 1
                    if node.right:
                        q.append(node.right)
                        new_lc +=1
                    
            if rightside:
                res.append(rightside.val)
            layer_count = new_lc
        return res
            