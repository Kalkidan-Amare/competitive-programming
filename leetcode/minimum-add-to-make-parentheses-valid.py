class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []

        for ele in s:
            if stack and ele == ')' and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(ele)
        
        return len(stack)