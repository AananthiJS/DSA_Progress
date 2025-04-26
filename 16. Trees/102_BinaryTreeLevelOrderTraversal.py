#APPROACH 1
#Using DFS

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root) :
        if not root:
            return []
        else:
            res = [[]]
            level = 0
    
            def dfs(root, level):
                # Using DFS
                # Base case
                if not root:
                    return
    
                if len(res) <= level:
                    res.append([])
    
                res[level].append(root.val)
                
                # Recursion
                root.left = dfs(root.left, level + 1)
                root.right = dfs(root.right, level + 1)
            
            dfs(root, 0) 
            return res