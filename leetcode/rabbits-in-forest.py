class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        count = Counter(answers)
        sum = 0
        for key,val in count.items():
            sum += (key + 1) * (math.ceil(val / (key+1)))

        return sum