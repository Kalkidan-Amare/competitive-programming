class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for ele in tokens:
            if ele.isnumeric() or ele[0] == '-' and ele[1:].isnumeric():
                stack.append(int(ele))
            elif ele == "+":
                x , y = stack.pop(), stack.pop()
                stack.append((y + x))
            elif ele == "-":
                x , y = stack.pop(), stack.pop()
                stack.append((y - x))
            elif ele == "*":
                print(stack)
                x , y = stack.pop(), stack.pop()
                stack.append((y * x))
            elif ele == "/":
                x , y = stack.pop(), stack.pop()
                stack.append(int(y / x))
        
        return stack.pop()
