class TreeNode:
    def __init__(self, val = 0):
        self.val = val
        self.left = None
        self.right = None

def findMin(root):
    cur = root
    while cur and cur.left:
        cur = cur.left
    return cur

def remove(root, target):
    # Base case
    if not root:
        return None
       
    # Recursion 
    if root.val > target:
        root.left = remove(root.left, target)
    elif root.val < target:
        root.right = remove(root.right, target)
    else:
        # Case 1
        if not root.left:
            return root.right
        elif not root.right:
            return root.left
        # Case 2
        else:
            minNode = findMin(root.right)
            root.val = minNode.val
            root.right = remove(root.right, minNode.val)
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
root.right = TreeNode(6)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)
root.right.right = TreeNode(7)

# remove(root, 4)
# remove (root, 6)
# remove(root, 3)

print_tree(root)