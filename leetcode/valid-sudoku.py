class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        m = len(board)
        setRow = set()
        setCol = set()
        setBox = set()

        for i in range(m):
            setRow.clear()
            setCol.clear()
            for j in range(m):
                curRow = board[i][j]
                if curRow != '.':
                    if curRow in setRow:
                        return False
                    setRow.add(curRow)
                curCol = board[j][i]
                if curCol != '.':
                    if curCol in setCol:
                        return False
                    setCol.add(curCol)
        
        m = n = 0
        while m < 9:
            setBox = set()
            for i in range(m,m+3):
                for j in range(n,n+3):
                    cur = board[i][j]
                    if cur != '.':
                        if cur in setBox:
                            return False
                        setBox.add(cur)

            n += 3
            if n == 9:
                n = 0
                m += 3

        return True

                