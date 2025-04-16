# NOTE:
# Mathematically speaking, a binary tree is a connected, undirected graph with no cycles.

# The property is that every node in the left subtree is smaller than the root and every node in the right subtree is greater than the
# root.
# This is a recursive property, meaning that it applies to every node in the tree. This property is analogous to having a sorted array.

# Why BST when we have sorted array?
# With BSTs we can search for values in O(logn) time just like with a sorted array.

# BSTs are often preferred over sorted arrays because they allow for insertion and deletion in O(log n) time. This is not possible with
# sorted arrays, which require, O(n) time for these operations.

def search(root, target):
    if not root:
        return False
    
    if target > root.val:
        return search(root.right, target)
    elif target < root.val:
        return search(root.left, target)
    else:
        return True
