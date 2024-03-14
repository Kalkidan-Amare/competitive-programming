class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        temp = [0] * (len(s)+1)

        for arr in shifts:
            if arr[2] == 0:
                temp[arr[0]] -= 1
                temp[arr[1]+1] += 1
            else:
                temp[arr[0]] += 1
                temp[arr[1]+1] -= 1
        
        prefix = list(accumulate(temp))

        ans = list(s)

        for i in range(len(s)):
            ans[i] = chr( ord('a')+ (ord(ans[i])-ord('a') + prefix[i])%26)
        
        return ''.join(ans)