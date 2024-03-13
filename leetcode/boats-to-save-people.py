class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        ans = 0 
        l , r = 0 , len(people)-1

        while l <= r:
            if people[l] + people[r] > limit:
                ans += 1
                r -= 1
            else:
                ans += 1
                r -= 1
                l += 1
        
        if l == r:
            return ans + 1
        return ans