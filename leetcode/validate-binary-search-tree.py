# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
   
        def helper(start,minn,maxx):
            if not start:
                return True
            
            valid = minn < start.val < maxx

            return valid and helper(start.left,minn,start.val) and helper(start.right,start.val,maxx)

        return helper(root,float('-inf'),float('inf'))
