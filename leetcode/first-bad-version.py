# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        l , r = 1, n
        mid = status = 0
        while l <= r:
            mid = (l+r)//2
            if isBadVersion(mid):
                status = 1
                r = mid -1
            else:
                status = 0
                l = mid + 1

        if status:
            return mid
        return mid + 1