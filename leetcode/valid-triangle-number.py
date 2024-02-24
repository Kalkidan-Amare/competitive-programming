class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        result = 0
        n = len(nums)

        for i in range(n-2):
            l,r = i+1,n-1
            while l < r:
                if nums[l] + nums[r] > nums[i]:
                    result += r - l
                    l += 1
                else:
                    r -= 1

        return result