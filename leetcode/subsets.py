class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        Allsets = []
        def helper(path,i):
            if i >= len(nums):
                Allsets.append(path[:])
                return
            
            helper(path,i+1)
            path.append(nums[i])
            
            helper(path,i+1)
            path.pop()

        helper([],0)

        return Allsets