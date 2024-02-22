class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        stack = []
        dictt = {}
        for ele in nums2:
            while stack and ele > stack[-1]:
                dictt[stack.pop()] = ele
            stack.append(ele)
        for ele in nums1:
            if ele in dictt:
                result.append(dictt[ele])
            else:
                result.append(-1)

        return result