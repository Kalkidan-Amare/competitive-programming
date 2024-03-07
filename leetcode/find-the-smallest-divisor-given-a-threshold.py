class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        low , high = 1, max(nums)

        while low <= high:
            total = 0
            mid = (low+high)//2
            for ele in nums:
                total += ceil(ele/mid)
            if total <= threshold:
                high = mid - 1
            else:
                low = mid + 1
            
        return low