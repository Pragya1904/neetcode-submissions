# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def dfr(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        lh = self.dfr(root.left)
        rh = self.dfr(root.right)

        return 1 + max(lh, rh)

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        if root is None:
            return 0
        
        lh = self.dfr(root.left)
        rh = self.dfr(root.right)

        curr_dia = lh + rh
        sub_dia = max(self.diameterOfBinaryTree(root.left), self.diameterOfBinaryTree(root.right))

        return max(curr_dia, sub_dia)
