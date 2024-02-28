# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def helper(start,minn = float('-inf'),maxx = float('inf')):
            if not start:
                return True
            
            left = minn < start.val < maxx and helper(start.left,minn,start.val)
            right = minn < start.val < maxx and helper(start.right,start.val,maxx)
            return left and right

        return helper(root)