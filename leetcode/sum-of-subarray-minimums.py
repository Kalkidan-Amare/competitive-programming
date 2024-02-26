class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        n = len(arr)
        stack = []
        leftSmaller = [-1] * n
        rightSmaller = [n] * n

        for i,val in enumerate(arr):
            while stack and val < arr[stack[-1]]:
                rightSmaller[stack.pop()] = i
            if stack:
                leftSmaller[i] = stack[-1]
            stack.append(i)
  
        result = 0
        for i in range(n):
            leftRange = i - leftSmaller[i] 
            rightRange = rightSmaller[i] - i
            result += arr[i] *( leftRange * rightRange)
    
        return (result)% ((10**9) + 7)