class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        n = len(palindrome)
        if n == 1:
            return ""
        li = list(palindrome)
        
        for i in range(n):
            if li[i] != 'a' and (n % 2 == 0 or i != n//2):
                li[i] = 'a'
                break
            elif i == n - 1:
                li[i] = 'b'

        return ''.join(li)