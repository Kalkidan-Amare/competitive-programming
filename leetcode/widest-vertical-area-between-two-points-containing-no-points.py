class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        xaxis = [x[0] for x in points]
        xaxis.sort()
        maxx = 0
        for i in range(1,len(xaxis)):
            maxx = max(maxx, xaxis[i]-xaxis[i-1])
        
        return maxx