# Problem: Image Smoother - https://leetcode.com/problems/image-smoother/description/

class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        r,c = len(img), len(img[0])
        smoothed_image = [[0] * c for _ in range(r)]

        for i in range(r):
            for j in range(c):
                sum = count = 0

                for n in range(i-1,i+2):
                    for m in range(j-1,j+2):
                        if 0 <= n < r and 0 <= m < c:
                            sum += img[n][m]
                            print(sum)
                            count += 1
                avg = sum // count
                smoothed_image[i][j] = avg

        return smoothed_image