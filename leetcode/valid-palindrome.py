class Solution:
    def isPalindrome(self, s: str) -> bool:
        li = [i for i in s.lower() if i.isalnum()]
        
        l , r = 0 , len(li) -1 
        while l < r:
            if li[l] != li[r]:
                return False
            l += 1
            r -= 1
        
        return True