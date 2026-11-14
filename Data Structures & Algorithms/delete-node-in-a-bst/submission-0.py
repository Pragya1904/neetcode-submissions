# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None
        
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            #key found

            # 0 or 1 child -> easy deletes
            if not root.right:
                return root.left
            elif not root.left:
                return root.right
            
            #both children are present
            #find the inorder sucessor or predecessor

            # pred largest element on the left subtree
            pred = root.left
            while pred.right:
                pred = pred.right
            
            root.val =  pred.val
            root.left = self.deleteNode(root.left, pred.val)
        
        return root
