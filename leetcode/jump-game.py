class Solution:
    def canJump(self, nums: List[int]) -> bool:
        step = nums[0]
        for i in range(1,len(nums)):
            if step == 0:
                return False
            step -= 1
            if step < nums[i]:
                step = nums[i]
        
        return True