class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dict1 = Counter(nums1)
        ans = []

        for ele in nums2:
            if ele in dict1:
                ans.append(ele)
                dict1[ele] -= 1
                if dict1[ele] == 0:
                    del dict1[ele]
        
        return ans
        