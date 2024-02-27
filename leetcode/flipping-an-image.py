class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        # li = [row[:] for row in image]
        # li = copy.deepcopy(image)

        for row in image:
            row.reverse()
            for i in range(len(row)):
                row[i] = 1 - row[i]
        
        return image