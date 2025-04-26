from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root):
        queue = deque()
        res = []

        if root:
            queue.append(root)

        # Loop through each level
        while len(queue) > 0:
            temp = []
            # Loop through each node in the level
            for i in range(len(queue)):
                cur = queue.popleft()
                temp.append(cur.val)

                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)

            res.append(temp[-1])

        return res
    
# # APPROACH 2
# # Using DFS

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root) :
        # Using DFS
        level = 0
        res = []

        def dfs(root, level):
            # Base case
            if not root:
                return None

            # Recursion
            if level == len(res):
                res.append(root.val)

            dfs(root.right, level + 1)
            dfs(root.left, level + 1)

        dfs(root, 0)
        return res
    
# Time complexity: O(n)
# Space complexity: O(n)
# n = number of nodes in the tree