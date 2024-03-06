class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        count=1
        for n in range(1,len(nums)):
            if nums[n] != nums[n-1]:
                nums[count] = nums[n]
                count+=1

        return count