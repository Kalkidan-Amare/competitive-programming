class Solution:

    def isPowerOfFour(self, n) -> bool:
        if n == 1:
            return True
        if n < 4:
            return False

        return self.isPowerOfFour(n/4)