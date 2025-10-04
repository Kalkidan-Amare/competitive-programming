# Problem: Longest Repeating Character Replacement - https://leetcode.com/problems/longest-repeating-character-replacement/

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = defaultdict(int)
        max_length = l = 0

        for r in range(len(s)):
            freq[s[r]] += 1
            max_freq = max(freq.values())
            cur_len = r - l + 1
            if cur_len - max_freq > k:
                freq[s[l]] -= 1
                l += 1
            
            max_length = max(max_length, r - l + 1)

        return max_length