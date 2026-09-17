# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
   
    def generateTrees(self, n: int) -> list[TreeNode | None]:

        def generate(start, end):

            # No nodes
            if start > end:
                return [None]

            all_trees = []

            # Try every number as root
            for root_value in range(start, end + 1):

                # Generate all possible left subtrees
                left_trees = generate(start, root_value - 1)

                # Generate all possible right subtrees
                right_trees = generate(root_value + 1, end)

                # Combine every left subtree with every right subtree
                for left in left_trees:
                    for right in right_trees:

                        root = TreeNode(root_value)

                        root.left = left
                        root.right = right

                        all_trees.append(root)

            return all_trees

        return generate(1, n)
