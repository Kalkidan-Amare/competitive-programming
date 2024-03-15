class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        dictt = defaultdict(int)
        dictt[0] = 1
        total = count = 0
        for ele in nums:
            total += ele
            if total - k in dictt:
                count += dictt[total - k]
            
            dictt[total] += 1
        
        return count