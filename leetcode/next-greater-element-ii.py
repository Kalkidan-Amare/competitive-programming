class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack = []
        result = [-1] * len(nums)

        for i in range(2):
            for j in range(len(nums)):
                while stack and nums[stack[-1]] < nums[j]:
                    result[stack.pop()] = nums[j]
                stack.append(j)
        
        return result
        
