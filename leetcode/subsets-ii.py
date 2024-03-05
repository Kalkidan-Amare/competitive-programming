class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = set()
        realAns = []

        def helper(path,idx):
            if idx == len(nums):
                ans.add(tuple(sorted(path[:])))
                return

            helper(path,idx + 1)
            path.append(nums[idx])
            helper(path,idx+1)
            path.pop()

        helper([],0)
        return sorted(ans)