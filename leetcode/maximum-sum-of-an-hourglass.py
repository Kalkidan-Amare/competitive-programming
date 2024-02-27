class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        maxx = float('-inf')

        for i in range(1,len(grid)-1):
            for j in range(1,len(grid[0])-1):
                total = 0
                total = grid[i][j] + sum(grid[i-1][j-1:j+2]) + sum(grid[i+1][j-1:j+2])
                maxx = max(maxx,total)
        
        return maxx