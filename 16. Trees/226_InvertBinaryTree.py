from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def invertTree(self, root) :
        # Creating a new tree and making the changes
        queue = deque()
        newQueue = deque()
        newRoot = None

        if root:
            queue.append(root)
            newRoot = TreeNode(root.val)
            newQueue.append(newRoot)

        while len(queue) > 0:
            for i in range(len(queue)):
                cur = queue.popleft()
                newCur = newQueue.popleft()
                if cur.right:
                    newCur.left = TreeNode(cur.right.val)
                    queue.append(cur.right)
                    newQueue.append(newCur.left)
                if cur.left:
                    newCur.right = TreeNode(cur.left.val)
                    queue.append(cur.left)
                    newQueue.append(newCur.right)

        return newRoot

# TC: O(n)
# SC: O(n) + O(h) + O(h) = O(n)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root):
        # Modify the original tree.
        queue = deque()

        if root:
            queue.append(root)

        while len(queue) > 0:
            for i in range(len(queue)):
                cur = queue.popleft()
                if cur.right:
                    queue.append(cur.right)
                if cur.left:
                    queue.append(cur.left)
                cur.right, cur.left = cur.left, cur.right
        return root
    
# TC: O(n)
# SC: O(w) 
# w = max width of the tree
# w = O(n) in the worst case
# w = O(log n) in the best case

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root) :
        # Using DFS
        # Base case
        if not root:
            return None

        # Recursion
        root.right, root.left = self.invertTree(root.left), self.invertTree(root.right)

        return root

# TC: O(n)
# SC: O(h)
# h = height of the tree
# O(n) if it's worst case

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Iterative DFS
        stack = [root]
        cur = root

        while stack:
            top = stack.pop()
            if top:
                top.left, top.right = top.right, top.left

                if top.left:
                    stack.append(top.left)
                if top.right:
                    stack.append(top.right)

        return root

# TC: O(n)
# SC: O(n)
# n is the number of nodes - stack