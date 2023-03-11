# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        from collections import deque
        
        def bfs(node):
            checklist = deque([node])
            
            while checklist:
                curr = checklist.popleft()
                if curr.val == target.val:
                    return curr
                else:
                    if curr.left:
                        checklist.append(curr.left)
                    if curr.right:
                        checklist.append(curr.right)
            
        return bfs(cloned)