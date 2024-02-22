class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        sum=0
        dig= []
        for n in digits:
            sum= (sum*10) + n 
        sum+=1
        while(sum):
            dig.insert(0,sum%10)
            sum//=10

        return dig