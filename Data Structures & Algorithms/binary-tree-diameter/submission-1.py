# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxHeight(self, root: Optional[Treenode]) -> int:
        if root is None:
            return 0
        
        return 1 + max(self.maxHeight(root.left), self.maxHeight(root.right))

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        
        
        left_height = self.maxHeight(root.left)
        right_height = self.maxHeight(root.right)

        curr_diameter = left_height + right_height
        subtree_dia = max(self.diameterOfBinaryTree(root.left), self.diameterOfBinaryTree(root.right))

        return max(curr_diameter, subtree_dia)