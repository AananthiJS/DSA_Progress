# APPROACH 1

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, preorder, inorder):
        # Base case
        if not preorder or not inorder:
            return None

        # Recursion
        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])

        root.left = self.buildTree(preorder[1 : mid + 1], inorder[: mid])
        root.right = self.buildTree(preorder[mid + 1: ], inorder[mid + 1: ])

        return root
    
# APPROACH 2

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder, inorder) :
        # Create hashmap instead of lookup
        indices = {val : idx for idx,val in enumerate(inorder)}
        # To keep track of the root
        self.pre_idx = 0 

        def dfs(l, r):
            # Base case
            if l > r:
                return None

            # Recursion
            root_val = preorder[self.pre_idx]
            self.pre_idx += 1
            root = TreeNode(root_val)
            mid = indices[root_val]

            root.left = dfs(l, mid - 1)
            root.right = dfs(mid + 1, r)

            return root
        return dfs(0, len(inorder) - 1)
    
# APPROACH 3

class Solution:
    def buildTree(self, preorder, inorder):
        # Two pointers
        self.preIndex, self.inIndex = 0, 0

        def dfs(limit):
            # Base case
            if self.preIndex >= len(preorder):
                return None

            if inorder[self.inIndex] == limit:
                self.inIndex += 1
                return None

            # Recursion
            root = TreeNode(preorder[self.preIndex])
            self.preIndex += 1

            root.left = dfs(root.val)
            root.right = dfs(limit)

            return root

        return dfs(float('inf'))