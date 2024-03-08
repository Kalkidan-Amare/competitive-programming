class Solution:
    def maxScore(self, s: str) -> int:
        prefix = list(accumulate(map(int,s)))
        print(prefix)
        
        ans = float('-inf')
        for i in range(len(prefix)-1):
            ans = max(ans,(i+1-prefix[i]) + (prefix[len(prefix)-1] - prefix[i]))

        return ans