class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        count= Counter(s)
        seen = set()
        ans = []
        l = 0
        for r in range(len(s)):
            seen.add(s[r])
            count[s[r]] -= 1

            if count[s[r]] == 0:
                seen.remove(s[r])

            if len(seen) == 0:
                ans.append(r+1-l)
                l = r + 1
        return ans