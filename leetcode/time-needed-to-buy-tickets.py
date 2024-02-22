class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        i = time = 0
        size = len(tickets)

        while tickets[k] > 0:
            if tickets[i] > 0:
                tickets[i] -= 1
                time += 1
            i = (i + 1) % size

        return time