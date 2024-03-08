# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        dict = defaultdict(int)

        def helper(root):
            if not root:
                return
            
            dict[root.val] += 1

            helper(root.left)
            helper(root.right)

        helper(root)
        
        ans = []
        temp = 0
        for key in dict:
            if dict[key] > temp:
                ans = []
                ans.append(key)
                temp = dict[key]
            elif dict[key] == temp:
                ans.append(key)

        return ans