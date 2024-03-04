class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        permutation = []
        visited = set()
        def helper(path):
            if len(path) == len(nums):
                permutation.append(path[:])
                return

            for ele in nums:
                if ele in path:
                    continue
                path.append(ele)
                visited.add(ele)    
                helper(path)
                path.pop()
                visited.remove(ele)

        helper([])

        return permutation