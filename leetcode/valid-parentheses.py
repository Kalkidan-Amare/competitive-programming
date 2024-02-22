class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        bracket={')':'(',']':'[','}':'{'}

        for c in s:
            if c in bracket.values():
                stack.append(c)
            elif c in bracket.keys():
                if not stack or bracket[c] != stack.pop():
                    return False
            else:
                return False
        
        return not stack