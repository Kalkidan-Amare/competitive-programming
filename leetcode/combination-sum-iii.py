class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans = []
        def helper(path,idx):
            if len(path) == k and sum(path) == n:
                ans.append(path[:])
          
            for i in range(idx,10):
                if sum(path) <= n:
                    path.append(i)
                    helper(path,i+1)
                    path.pop()

        helper([],1)

        return ans

