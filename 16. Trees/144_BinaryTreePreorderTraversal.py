class Solution:
    def preorderTraversal(self, root):
        output = []

        def preorder(root):
            # Base case
            if not root:
                return None

            # Recursion [TC: O(n)]
            output.append(root.val)
            preorder(root.left)
            preorder(root.right)

        preorder(root)
        return output
    
# TC: O(n)
# SC: O(n)

# In recursion:
# Every function call gets pushed onto the call stack.
# Most systems have a maximum call stack size (like 1000 to 3000 frames depending on language/environment).
# So if your tree is really deep (like skewed to one side), recursion can cause:
# ❌ StackOverflowError (yes, that’s where the website name came from!)
# In production environments with large trees, iterative solutions can be more memory-efficient since they don't hit recursion depth limits.”
# The explicit stack you create (like stack = []) lives in the heap memory, which is much larger and managed more flexibly.

class Solution:
    def preorderTraversal(self, root):
        # Iterative DFS
        cur = root # SC: O(1)
        stack = [] # SC: O(n)
        output = [] # SC: O(n)

        while cur or stack: # TC: O(n)
            if cur:
                # go left and store right to come back
                output.append(cur.val)
                stack.append(cur.right)
                cur = cur.left
            else:
                cur = stack.pop()

        return output

# TC: O(n) - Touches every node only once
# SC: O(n)
# n = number of nodes in the tree