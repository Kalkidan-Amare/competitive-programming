class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        def helper(path,open,close):
            if len(path) == n*2:
                ans.append(''.join(path))
                return

            if open < n:
                path.append('(')
                helper(path, open + 1 ,close)
                path.pop()
            
            if close < open:
                path.append(')')
                helper(path,open,close+1)
                path.pop()
            

        helper([],0,0)

        return ans