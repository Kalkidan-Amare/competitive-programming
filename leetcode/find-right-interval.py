class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        ans = []
        
        firstIndices = [ele[0] for ele in intervals]
        firstIndices.sort()

        dictt = {}
        for i,ele in enumerate(intervals):
            dictt[ele[0]] = i

        for ele in intervals:
            temp = bisect_left(firstIndices,ele[1])
            if temp < len(firstIndices):
                ans.append(dictt[firstIndices[temp]])
            else:
                ans.append(-1)
        
        return ans

        
        

        