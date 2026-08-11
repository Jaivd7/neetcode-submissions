# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # Preorder is root left right
        # Inorder is left root right
        # if not preorder or not inorder:
        #     return None

        # root = TreeNode(preorder[0])
        # mid = inorder.index(preorder[0])
        # root.left = self.buildTree(preorder[1 : mid + 1], inorder[:mid])
        # root.right = self.buildTree(preorder[mid + 1 :], inorder[mid + 1 :])
        # return root
        hmap = {}
        for i in range(len(inorder)):
            key = inorder[i]
            hmap[key] = i
        

        def buildtree2(ps, pe, ins, ine):
            if ps>= pe or ins>= ine:
                return None
            root = TreeNode(preorder[ps])
            mid = hmap[preorder[ps]]
            left_size = mid - ins
            root.left = buildtree2(ps + 1, ps + 1 + left_size, ins, mid)
            root.right = buildtree2(ps + 1 + left_size, pe, mid + 1, ine)
            return root

        return buildtree2(0, len(preorder), 0, len(inorder))
