# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root) :
        output = []
        def inorder(root):
            # Base case
            if not root:
                return []

            # Recursion
            inorder(root.left)
            output.append(root.val)
            inorder(root.right)
            return output
        return inorder(root)