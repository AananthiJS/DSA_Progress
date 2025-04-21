#NOTE: left, root, right

class TreeNode:
    def __init__(self, val = 0):
        self.val = val
        self.left = None
        self.right = None

def inorder(root):
    if not root:
        return None

    inorder(root.left)
    print(root.val)
    inorder(root.right)

# Main
root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(9)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)
root.right.right = TreeNode(7)

inorder(root)