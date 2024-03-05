class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        ans = 0
        for ele in costs:
            if ele > coins:
                return ans
            coins -= ele
            ans += 1
        
        return ans