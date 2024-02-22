class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack1 = []
        stack2 = []

        for ele in s:
            if stack1 and ele == '#':
                stack1.pop()
            elif ele != '#':
                stack1.append(ele)
        for ele in t:
            if stack2 and ele == '#':
                stack2.pop()
            elif ele != '#':
                stack2.append(ele) 
        
        return stack1 == stack2