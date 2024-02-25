class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        total = result = 0
        nums.append(n)
        for ele in nums:
            while ele > total + 1 and total < n:
                result += 1
                total += total + 1
            else:
                total += ele
        
        return result