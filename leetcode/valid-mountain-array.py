class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        lenn = len(arr)
        if lenn < 3:
            return False
        l , r = 0 , lenn -1 
        while l < lenn-1 and arr[l] < arr[l+1]:
            l += 1
        while arr[r] < arr[r-1] and r > 0:
            r -= 1
        return l == r and l != 0 and r != lenn-1