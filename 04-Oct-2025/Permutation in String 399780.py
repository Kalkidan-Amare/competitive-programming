# Problem: Permutation in String - https://leetcode.com/problems/permutation-in-string/

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        permutation_count = Counter(s1)

        substring_count = defaultdict(int)

        l = 0
        for r in range(len(s1)-1):
            substring_count[s2[r]] += 1
        # print(permutation_count)
        # print(substring_count)

        for r in range(len(s1)-1,len(s2)):
            substring_count[s2[r]] += 1
            # print(substring_count)
            if substring_count == permutation_count:
                return True
            
            substring_count[s2[l]] -= 1
            if substring_count[s2[l]] == 0:
                del substring_count[s2[l]]
            l += 1

        return False
