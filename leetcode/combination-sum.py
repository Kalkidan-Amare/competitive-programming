class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        combination = set()
        
        def helper(path,i,total):
            if total == target:
                combination.add(tuple(sorted(path[:])))
                return

            for ele in candidates:
                if total + ele <= target:
                    path.append(ele)
                    helper(path,i+1,total+ele)
                    path.pop()

        helper([],0,0)

        return combination