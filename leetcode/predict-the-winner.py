class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        
        def helper(l,r,turn):
            if l == r:
                return [nums[l],0] if turn else [0,nums[l]]

            p1l,p2l = helper(l+1,r,not turn)
            p1r,p2r = helper(l,r-1,not turn)

            if turn:
                p1l += nums[l]
                p1r += nums[r]
                if p1l > p1r:
                    return [p1l,p2l]
                return [p1r,p2r]
            else:
                p2l += nums[l]
                p2r += nums[r]
                if p2l > p2r:
                    return [p1l,p2l]
                return [p1r,p2r]


        p1,p2= helper(0,len(nums)-1,True)

        return p1 - p2 >= 0 