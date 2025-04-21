class TreeNode:
    def __init__(self, val = 0):
        self.val = val
        self.left = None
        self.right = None

def insert(root, val):
    # Base case
    if not root:
        return TreeNode(val)
        
    # /Recursion
    if root.val > val:
        root.left = insert(root.left, val)
    elif root.val < val:
        root.right = insert(root.right, val)
    return root

def print_tree(node, indent = "", position = "Root"):
    if node:
        print(f"{indent}[{position}] - {node.val}")
        indent += "      "
        print_tree(node.left, indent, "L")
        print_tree(node.right, indent, "R")

# Main
root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(9)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)
root.right.right = TreeNode(7)

insert(root, 8)
insert(root, 6)

print_tree(root)