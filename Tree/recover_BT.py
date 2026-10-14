# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: TreeNode | None) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        
class Solution:
    def recoverTree(self, root: TreeNode | None) -> None:
        prev = None
        first = None
        second = None

        def inorder(node):
            nonlocal prev, first, second

            if node is None:
                return

            
            inorder(node.left)

        
            if prev is not None and prev.val > node.val:
                if first is None:
                    first = prev

                second = node

            
            prev = node

           
            inorder(node.right)

        inorder(root)

        # Swap the two incorrect values
        first.val, second.val = second.val, first.val
