class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        greater, smaller,equal = [], [], []

        for ele in nums:
            if ele < pivot:
                smaller.append(ele)
            elif ele > pivot:
                greater.append(ele)
            else:
                equal.append(ele)
        
        return smaller + equal + greater