class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        positive, negative = [], []
        result = []

        for ele in nums:
            if ele > 0:
                positive.append(ele)
            else:
                negative.append(ele)
        for i in range(len(positive)):
            result.append(positive[i])
            result.append(negative[i])
        
        return result