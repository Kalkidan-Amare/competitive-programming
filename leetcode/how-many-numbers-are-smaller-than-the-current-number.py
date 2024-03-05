class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sortedNum=sorted(nums)
        count = Counter(sortedNum)
        ans = []
        for ele in nums:
            temp = 0
            for key in count:
                if key == ele:
                    break
                temp += count[key]
            ans.append(temp)

        return ans
