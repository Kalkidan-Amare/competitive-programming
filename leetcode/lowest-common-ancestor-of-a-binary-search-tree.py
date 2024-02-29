# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        def helper(start,a,b):
            if not start:
                return

            if start.val == a.val or start.val == b.val:
                return start
            
            left = helper(start.left,a,b)
            right = helper(start.right,a,b)
            
            if left and right:
                return start
            elif left:
                return left
            return right
            
        return helper(root,p,q)