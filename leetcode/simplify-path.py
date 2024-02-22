class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        symbol = ['.','..','',]
        path = path.split('/')

        for ele in path:
            if ele not in symbol:
                stack.append(ele)
            if ele == '..' and len(stack) > 0:
                stack.pop()
        
        return '/' + '/'.join(stack)