from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root) -> int:
        queue = deque()
        level = 0

        if root:
            queue.append(root)

        while len(queue) > 0:
            for i in range(len(queue)):
                node = queue.popleft()
                if node:
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
            level += 1

        return level

# TC: O(n)
# SC: O(n)
# n = number of nodes in the tree
# best case: O(w) 
# w is the width of the tree

class Solution:
    def maxDepth(self, root) -> int:
        # Recursive DFS
        # Base case
        if not root:
            return 0

        # Recursion
        level = 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
        return level

# TC: O(n)
# SC: O(n)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root) -> int:
        # Iterative DFS
        stack = [[root, 1]] # [node, depth]
        level = 0

        while stack:
            node, depth = stack.pop()

            if node:
                level = max(level, depth)
                stack.append([node.left, depth + 1])
                stack.append([node.right, depth + 1])
            
        return level

# TC: O(n)
# SC: O(n)