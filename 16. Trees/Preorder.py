#NOTE: root, left, right


class TreeNode:
    def __init__(self, val = 0):
        self.val = val
        self.left = None
        self.right = None

def preorder(root):
    if root:
        print(root.val)
        preorder(root.left)
        preorder(root.right)

# Main
root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(9)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)
root.right.right = TreeNode(7)

preorder(root)