class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        dictt = defaultdict(int)
        dictt[0] = 1

        count = total = 0

        for ele in nums:
            total += ele
            if (total - k)%k in dictt:
                count += dictt[(total - k)%k]
            
            dictt[total%k] += 1
        
        return count