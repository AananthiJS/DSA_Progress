# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root) :
        res = []

        def postorder(root):
            # Base case
            if not root:
                return None

            # Recursion
            postorder(root.left)
            postorder(root.right)
            res.append(root.val)

        postorder(root)
        return res
    
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root) :
        # Iterative DFS
        stack = []
        preorder_list = []
        last_visited = None
        cur = root

        while cur or stack:
            # Appending all left nodes
            while cur:
                stack.append(cur)
                cur = cur.left
            top = stack[-1]
            if top.right and (last_visited != top.right):
                cur = top.right
                continue
            preorder_list.append(top.val)
            last_visited = top
            stack.pop()
            cur = None

        return preorder_list
    
# TC: O(n)
# SC: O(n)