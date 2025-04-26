# Also known as Level order traversal
# Layer by layer
# Iterative
# Using Queue

from collections import deque
class Solution:
    def levelOrder(self, root) :
        queue = deque()
        res = [] 

        if root:
            queue.append(root)
            
        # loop through each level
        while len(queue) > 0:
            temp = []
            # loop through elements in that level
            for i in range(len(queue)):
                cur = queue.popleft()
                temp.append(cur.val)
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
            res.append(temp)

        return res

