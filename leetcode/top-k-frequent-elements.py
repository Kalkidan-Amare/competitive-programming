class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        maxx = max(count.values())
        minn = min(count.values())

        bucket = [[] for _ in range(maxx)]
        
        
        for key,val in count.items():
            bucket[val-1].append(key)
    
        temp = k
        ans = []
        while len(ans) <= temp and k > 0:
            maxx -= 1
            if len(bucket[maxx]) <= k:
                ans.extend(bucket[maxx])
            else:
                ans.extend(bucket[maxx][:k+1])
            k -= len(bucket[maxx])

        return ans