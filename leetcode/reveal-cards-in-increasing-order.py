class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort(reverse=True)

        result = deque()

        for ele in deck:
            if not result:
                result.append(ele)
            elif len(result) == 1:
                result.appendleft(ele)
            else:
                result.appendleft(result.pop())
                result.appendleft(ele)
        return result