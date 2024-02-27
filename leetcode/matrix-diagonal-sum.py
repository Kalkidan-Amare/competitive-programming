class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        m = len(mat)
        dict = defaultdict(int)
        dictRev = defaultdict(int)

        for i in range(m):
            for j in range(m):
                dict[i-j] += mat[i][j]
                dictRev[i+j] += mat[i][j]
        
        total = dict[0] + dictRev[len(mat)-1]
        if m % 2 == 1:
            total -= mat[m//2][m//2]
        
        return total