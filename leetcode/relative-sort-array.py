class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        count = Counter(arr1)
        ans = []
        for ele in arr2:
            for i in range(count[ele]):
                ans.append(ele)
        
        ans2 = []
        arr2 = set(arr2)
        for ele in arr1:
            if ele not in arr2:
                ans2.append(ele)
        ans2.sort()

        return ans + ans2