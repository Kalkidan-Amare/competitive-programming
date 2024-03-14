class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowel = set(['a','e','i','o','u'])
       
        maxx = count = len([i for i in s[:k] if i in vowel])
       
        for r in range(k,len(s)):
            if s[r-k] in vowel:
                count -= 1
            if s[r] in vowel:
                count += 1
            
            maxx = max(maxx,count) 
        
        return maxx