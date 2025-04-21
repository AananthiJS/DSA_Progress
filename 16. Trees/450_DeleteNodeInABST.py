# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def findMin(self, root):
        cur = root
        while cur and cur.left:
            cur = cur.left
        return cur

    def deleteNode(self, root, key: int) :
        # Base case
        if not root:
            return None
        
        # Recursion
        if root.val > key:
            root.left = self.deleteNode(root.left, key)
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        else:
            # case 1
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            # case 2
            else:
                minNode = self.findMin(root.right)
                root.val = minNode.val
                root.right = self.deleteNode(root.right, minNode.val)
        return root