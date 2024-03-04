class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        combinations = []
        def helper(path,curr):
            if len(path) >= k:
                combinations.append(path[:])
                return
            
            for i in range(curr,n+1):
                path.append(i)
                helper(path,i+1)
                path.pop()
        
        helper([],1)

        return combinations