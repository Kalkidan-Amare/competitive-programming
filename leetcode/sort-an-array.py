class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        def merge(left_half,right_half) -> List[int]:
            mereged = []
            l = r = 0
            while l < len(left_half) and r < len(right_half):
                if left_half[l] < right_half[r]:
                    mereged.append(left_half[l])
                    l += 1
                else:
                    mereged.append(right_half[r])
                    r += 1
            mereged.extend(left_half[l:])
            mereged.extend(right_half[r:])
            
            return mereged


        def meregesort(left,right,nums):
            if left == right:
                return [nums[left]]
            
            mid = (left+right)//2
            left_part = meregesort(left,mid,nums)
            right_part = meregesort(mid+1,right,nums)

            return merge(left_part,right_part)


        return meregesort(0,len(nums)-1,nums)