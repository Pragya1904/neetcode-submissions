# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSame(self, a: Optional[TreeNode], b: TreeNode | None):
        if not a and not b:
            return True
        
        if (not a and b) or (not b and a):
            return False
        
        if a.val != b.val:
            return False
        
        left = self.isSame(a.left, b.left)
        right = self.isSame(a.right, b.right)

        return left and right

    def find(self, root: Optional[TreeNode], sub: Optional[TreeNode]):
        if not sub:
            return True
        if not root:
            return False
        
        if self.isSame(root, sub):
            return True
        
        return self.find(root.left, sub) or self.find(root.right, sub)

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        return self.find(root, subRoot)
        