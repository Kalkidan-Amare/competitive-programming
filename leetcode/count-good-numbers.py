class Solution:
    def helper(self,n):
        mod = 10**9+7
        if n <= 1:
            return 20
        if n % 2 == 0:
            return (self.helper(n//2)**2) % mod
        else:
            n -= 1
            return ((self.helper(n//2)**2) * 20) % mod

    def countGoodNumbers(self, n: int) -> int:
        if n == 1:
            return 5
        mod = 10**9+7
        if n % 2:
            n -= 1
            return (self.helper(n/2)*5) % mod
        return self.helper(n/2) % mod