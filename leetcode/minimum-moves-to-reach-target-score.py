class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        increment = double = 0

        while target > 1:
            if target % 2 == 0 and maxDoubles:
                target /= 2
                double += 1
                maxDoubles -= 1
            else:
                if maxDoubles == 0:
                    increment += target - 1
                    break
                target -= 1
                increment += 1
        
        return int(double + increment)