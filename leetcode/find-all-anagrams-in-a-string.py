class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ans = []
        if len(p) > len(s):
            return ans

        count = Counter(p)
        sliding_dict = Counter(s[:len(p)])

        l , r = 0, len(p)

        while r < len(s) :
            if sliding_dict == count:
                ans.append(l)
            sliding_dict[s[l]] -= 1

            if not sliding_dict[s[l]]:
                del sliding_dict[s[l]]
            
            if s[r] not in sliding_dict:
                sliding_dict[s[r]] = 1
            else:
                sliding_dict[s[r]] += 1

            r += 1
            l += 1
        
        if sliding_dict == count:
                ans.append(l)
        
        return ans


