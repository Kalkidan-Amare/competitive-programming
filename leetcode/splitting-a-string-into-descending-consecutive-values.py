class Solution:
    def splitString(self, s: str) -> bool:
        
        def helper(start,path):
            if start == len(s):
                return len(path) >= 2
            
            for i in range(start,len(s)):
                splitted = int(s[start:i+1])
                if path and splitted != path[-1] - 1:
                    continue
                path.append(splitted)
                if helper(i+1,path):
                    return True
                path.pop()
            
            return False #not necessary

        return helper(0,[])