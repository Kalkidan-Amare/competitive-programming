class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        
        pointer1 = pointer2 = 0
        
        while pointer1 < len(nums1) and pointer2 < len(nums2):
            n1 = nums1[pointer1]
            n2 = nums2[pointer2]
            if n1 == n2:
                return n1
            elif n1 > n2:
                pointer2 += 1
            else:
                pointer1 += 1

        return -1

