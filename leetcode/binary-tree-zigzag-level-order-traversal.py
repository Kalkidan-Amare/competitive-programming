# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        dict = defaultdict(list)
        def helper(curr, level):
            if not curr:
                return
            
            dict[level].append(curr.val)
            helper(curr.left, level + 1)
            helper(curr.right, level + 1)

        helper(root,0)

        li = [val if key%2 == 0 else val[::-1] for key,val in dict.items()]
        
        return li