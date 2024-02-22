class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        l,r = 0,sum(nums)
        arr = [0]
        max = r

        for i in range(len(nums)):
            if nums[i] == 0:
                l += 1
            else:
                r -= 1
            temp = l + r
            if temp == max:
                arr.append(i+1)
            elif temp > max:
                arr.clear()
                arr.append(i+1)
                max = temp
        return arr