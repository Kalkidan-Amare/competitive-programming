class Solution:
    def checker(self,capacity,days,weights):
        temp = 0
        for r in range(len(weights)):
            if temp + weights[r] > capacity:
                days -= 1
                temp = 0
            temp += weights[r]
            if not days:
                return False
        return True
    
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        minn,maxx = max(weights),sum(weights)

        while minn <= maxx:
            mid = (minn+maxx)//2
            if self.checker(mid,days,weights):
                maxx = mid - 1
                ans = mid
            else:
                minn = mid + 1

        print(minn,maxx)
        return minn