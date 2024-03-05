class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort(reverse=True)
        index = 1
        sum = 0
        for i in range(len(piles)//3):
            sum += piles[index]
            index += 2

        return sum