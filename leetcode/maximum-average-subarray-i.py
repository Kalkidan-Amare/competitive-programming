class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        ans = float('-inf')
        l , r = 0 , k -1
        temp = sum(nums[l:r])

        while r < len(nums):
            temp += nums[r]
            ans = max(ans, temp/k)
            temp -= nums[l]
            l += 1
            r += 1
            
        
        return ans