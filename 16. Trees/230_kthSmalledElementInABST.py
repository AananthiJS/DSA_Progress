#APPROACH 1

class Solution:
    def kthSmallest(self, root, k: int) -> int:
        # Inorder traversal to make a ascending ordered list
        inorder_list = []

        def inorder(root):
            if not root:
                return None
            inorder(root.left)
            inorder_list.append(root.val)
            inorder(root.right)

            return inorder_list

        # Get the kth value
        inorder_list = inorder(root)
        return inorder_list[k-1]
    
#APPROACH 2

class Solution:
    def kthSmallest(self, root, k: int):
        stack = []
        n = 0
        cur = root

        while stack or cur:
            # Go to the left most child and append the visited nodes to stack to fall back
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            n += 1
            if n == k:
                return cur.val
            cur = cur.right