class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        answer = [0] * len(temperatures)
        
        for index,ele in enumerate(temperatures):
            while stack and ele > stack[-1][1]:
                i,e = stack.pop()
                answer[i] = index-i
            stack.append((index,ele))  
        
        return answer