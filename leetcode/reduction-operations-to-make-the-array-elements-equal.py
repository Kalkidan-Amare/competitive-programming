class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        nums.sort()
        count = Counter(nums)
        li = []
        liset = set()
        for ele in nums:
            if ele not in liset:
                liset.add(ele)
                li.append(ele)

        ans = 0
        for i in range(len(count)):
            ans += i * count[li[i]]
        
        return ans


            
        