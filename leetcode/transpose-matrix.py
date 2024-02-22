class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        row,col = len(matrix),len(matrix[0])
        # arr = [[0]*row for i in range(col)]
        # for i in range(row):
        #     for j in range(col):
        #         arr[j][i] = matrix[i][j]
        arr = []
        for i in range(col):
            temp = []
            for j in range(row):
                temp.append(matrix[j][i])
            arr.append(temp)
        return arr