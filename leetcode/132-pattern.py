class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stackG = []
        greater = [[float('inf'),0] for i in range(len(nums))]

        for i in range(len(nums)-1,-1,-1):
            while stackG and nums[stackG[-1]] < nums[i]:
                greater[stackG.pop()][0] = (nums[i],i)
            stackG.append(i)
        minn = float('inf')
    
        for i in range(len(nums)):
            minn = min(minn,nums[i])
            greater[i][1] = minn
    
        for i,ele in enumerate(greater):
            if ele[0] != float(inf) and greater[ele[0][1]][1] < nums[i]:
                return True
       