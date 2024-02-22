class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        dictt = {}
        row = len(mat)
        col = len(mat[0])
        result = []
        for i in range(row):
            for j in range(col):
                if i + j in dictt:
                    dictt[i+j].append(mat[i][j])
                else:
                    dictt[i+j] = [mat[i][j]]
        for k,v in dictt.items():
            if k % 2 == 0:
                print(v)
                result.extend(v[::-1])
            else:
                print(v)
                result.extend(v)
        return result