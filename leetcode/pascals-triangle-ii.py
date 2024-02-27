from typing import List

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        if rowIndex == 1:
            return [1,1]

        prevrow = self.getRow(rowIndex - 1)
        li = [1] * (rowIndex + 1)
        for j in range(1,rowIndex):
            li[j] = prevrow[j-1] + prevrow[j]

        return li
