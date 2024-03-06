class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l , r = 0, len(nums)-1
        mid = 0
        ans = [-1,-1]
        while l <= r:
            mid = (l+r)//2
            if target == nums[mid]:
                ans[0]= mid
                r = mid -1
            elif target < nums[mid]:
                r = mid -1
            else:
                l = mid + 1
      
        l = 0
        r = len(nums) -1

        while l <= r:
            mid = (l+r)//2
            if target == nums[mid]:
                ans[1] = mid
                l = mid + 1
            if target < nums[mid]:
                r = mid - 1
            else:
                l = mid + 1
        
        return ans