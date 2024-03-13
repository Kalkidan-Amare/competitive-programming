class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        count = l = ans = 0

        for r in range(len(nums)):
            if nums[r] == 0:
                count += 1
            while count == k+1:
                if nums[l] == 0:
                    count -= 1
                l += 1
            
            ans = max(ans,r - l + 1)

        return ans