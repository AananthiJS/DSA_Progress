# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root):
        self.inorder_recursion = []
        self.inorder_list = self.inorder(root)
        self.num = 0

    def next(self) -> int:
        self.num += 1
        return self.inorder_list[self.num - 1]

    def hasNext(self) -> bool:
        if len(self.inorder_list) > self.num:
            return True
        return False
        
    def inorder(self, root):
        # Base case
        if not root:
            return None

        # Recursion
        self.inorder(root.left)
        self.inorder_recursion.append(root.val)
        self.inorder(root.right)

        return self.inorder_recursion

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root):
        self.inorder_list = []
        self.num = 0
        
        def dfs(root):
            # Iterative DFS
            stack = []
            cur = root
            
            while cur or stack:
                while cur:
                    stack.append(cur)
                    cur = cur.left
                cur = stack.pop()
                self.inorder_list.append(cur.val)
                cur = cur.right
            
        dfs(root)

    def next(self) -> int:
        self.num += 1
        return self.inorder_list[self.num - 1]

    def hasNext(self) -> bool:
        return self.num < len(self.inorder_list)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root):
        self.stack = []
        cur = root

        while cur:
            self.stack.append(cur)
            cur = cur.left

    def next(self) -> int:
        res = self.stack.pop()
        cur = res.right
        while cur:
            self.stack.append(cur)
            cur = cur.left
        return res.val

    def hasNext(self) -> bool:
        return bool(self.stack)
        

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root):
        self.stack = []
        self.cur = root

    def next(self) -> int:
        while self.cur:
            self.stack.append(self.cur)
            self.cur = self.cur.left
        self.cur = self.stack.pop()
        self.value = self.cur.val
        self.cur = self.cur.right

        return self.value

    def hasNext(self) -> bool:
        return bool(self.cur) or bool(self.stack)


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()