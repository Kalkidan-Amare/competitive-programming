class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        p1 = p2 = float('inf')

        for n in nums:
            if n <= p1:
                p1 = n
            elif n <= p2:
                p2 = n
            else:
                return True
        
        return False