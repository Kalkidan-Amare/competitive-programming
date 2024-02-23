class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = Counter(s)
        result ,odd, status = 0,0,False
    
        for val in count.values():
            if val % 2 == 0:
                result += val
            else:
                status = True
                result += val - 1
        
        return result + 1 if status else result