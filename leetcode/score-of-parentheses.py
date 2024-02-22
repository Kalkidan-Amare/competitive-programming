class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []
        
        for ele in s:
            if ele == '(':
                stack.append(ele)
            else:
                num = 0
                while stack[-1] != '(':
                    num += stack.pop()
                stack.pop()
                if num == 0:
                    num = 1
                else:
                    num *= 2
                stack.append(num)
            
        return sum(stack) 