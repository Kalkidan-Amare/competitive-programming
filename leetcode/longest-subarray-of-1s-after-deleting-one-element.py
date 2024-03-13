class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        ans = count = l = 0
   
        for r in range(len(nums)):
            if nums[r] == 0:
                count += 1

            while count == 2:
                if nums[l] == 0:
                    count -= 1
                l += 1
            
            
            ans = max(ans,r - l)
        
        return ans