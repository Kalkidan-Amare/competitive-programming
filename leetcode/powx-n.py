class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n < 0:
            return 1 / self.myPow(x,-1 * n)
        if n % 2:
            return x * self.myPow(x,n//2)**2
        result = self.myPow(x,n//2)
        return result*result