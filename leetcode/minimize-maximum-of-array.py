class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        maxx = nums[0]
        sum = maxx

        for i in range(1,len(nums)):
            sum += nums[i]
            avg = ceil(sum / (i+1))
            maxx = max(maxx,avg)
        
        return maxx