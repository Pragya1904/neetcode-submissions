# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if (not p and q) or (not q and p) :
            return False
        elif p is None and q is None:
            return True
        elif p and q:
            if p.val != q.val:
                return False
            else:
                left = self.isSameTree(p.left, q.left)
                right = self.isSameTree(p.right, q.right)
                print(f"{p.val} {q.val}")
                print(left)
                print(right)
                return left and right
    
