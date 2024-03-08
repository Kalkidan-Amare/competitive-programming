class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        n = len(nums)
        count = 0
        for i in range(n-1):
            r = i + 1
            while r < n:
                if nums[i] + nums[r] < target:
                    count += 1
                r += 1
        
        return count