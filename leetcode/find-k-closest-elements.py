class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l , r = 0, len(arr) - 1
        
        while l <= r:
            mid = (r+l)//2
            if arr[mid] == x:
                l = mid
                r = mid -1
                break
            elif arr[mid] > x:
                r = mid -1
            else:
                l = mid + 1

        ans = []
        while len(ans) < k:
            if r < 0:
                ans.append(arr[l])
                l += 1
            elif l > len(arr) - 1:
                ans.append(arr[r])
                r -= 1
            elif abs(x-arr[l]) < abs(x-arr[r]):
                ans.append(arr[l])
                l += 1
            else:
                ans.append(arr[r])
                r -= 1

        ans.sort()
        return ans