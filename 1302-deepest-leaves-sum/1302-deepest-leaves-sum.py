# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        q, parent = [root], []
        while q:
            parent, q = q, [node for p in q for node in [p.left, p.right] if node]

        return sum(p.val for p in parent)