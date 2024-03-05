class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ans = []
        def helper(path,idx,total):
            if total == target:
                ans.append(path[:])
                return
            
            for i in range(idx,len(candidates)):
                if i > idx and candidates[i] == candidates[i-1] or total > target:
                    continue
                path.append(candidates[i])
                helper(path,i+1,total + candidates[i])
                path.pop()
        
        helper([],0,0)

        return ans