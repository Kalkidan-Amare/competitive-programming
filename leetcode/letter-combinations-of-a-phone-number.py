class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        dict = {'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        ans = []
        def helper(path,idx):
            if len(path) == len(digits):
                ans.append("".join(path))
                return

            for i in range(idx,len(digits)):
                for j in range(len(dict[digits[i]])):
                    path.append(dict[digits[i]][j])
                    helper(path,i+1)
                    path.pop()

        helper([],0)

        return ans