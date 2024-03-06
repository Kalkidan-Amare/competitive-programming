class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        minn , maxx = 1,max(piles)

        def checker(k,h):
            for ele in piles:
                h -= ceil(ele/k)
                if h < 0:
                    return False
            return True

        while minn <= maxx:
            mid = (minn+maxx)//2
            if checker(mid,h):
                maxx = mid - 1
            else:
                minn = mid + 1
        
        return minn