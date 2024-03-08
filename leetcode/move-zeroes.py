class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        for ele in nums:
            if ele != 0:
                nums[i] = ele
                i += 1
        
        while i < len(nums):
            nums[i] = 0
            i += 1
        
        return nums