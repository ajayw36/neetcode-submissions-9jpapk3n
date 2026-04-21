# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorder_successor(self, root):
        if not root.left: return root
        else: return self.inorder_successor(root.left)
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root: return None
        if key == root.val:
            if root.left and root.right:
                successor = self.inorder_successor(root.right)
                successor.left = root.left
                return root.right
            elif root.left: return root.left
            else: return root.right
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            root.left = self.deleteNode(root.left, key)
        return root
                