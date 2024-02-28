class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        dict = {}
        for i in range(len(heights)):
            dict[heights[i]] = names[i]
        
        heights.sort(reverse=True)
       
        for i,ele in enumerate(heights):
            names[i],dict[ele] = dict[ele],names[i]
        
        return names