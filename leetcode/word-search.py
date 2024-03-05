class Solution:
    def inBound(self,row,col,i,j):
        return 0 <= i < row and 0 <= j < col

    def exist(self, board: List[List[str]], word: str) -> bool:
               
        visited = set()
        def helper(idxWord,row,col):
            if idxWord == len(word):
                return True

            directions = [[-1,0],[1,0],[0,1],[0,-1]]

            for x,y in directions:
                i = row + x
                j = col + y
                if (i,j) not in visited and self.inBound(len(board),len(board[0]),i,j) and board[i][j] == word[idxWord]:
                    visited.add((i,j))
                    if helper(idxWord+1,i,j):
                        return True
                    visited.discard((i,j))

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]: 
                    visited.add((i,j))
                    if helper(1,i,j):
                        return True
                    visited.discard((i,j))
        