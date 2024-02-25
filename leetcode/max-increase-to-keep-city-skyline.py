class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        maxRow, maxCol,result,n = [], [], 0, len(grid)
        
        for ele in grid:
            maxRow.append(max(ele))
        
        for i in range(n):
            maxx = -1
            for j in range(n):
                maxx = max(maxx,grid[j][i])
            maxCol.append(maxx)
        
        for i in range(n):
            for j in range(n):
                result += min(maxRow[i],maxCol[j]) - grid[i][j]
        print(maxRow)
        print(maxCol)
        
        return result