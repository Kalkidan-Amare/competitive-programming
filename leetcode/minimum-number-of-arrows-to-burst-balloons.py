class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        sortedArr = sorted(points,key = lambda x:x[1])
        l, r = 0, 1
        count = 0

        while r < len(sortedArr):
            if sortedArr[l][1] < sortedArr[r][0]:
                count += 1
                l = r
            r += 1

        return count + 1