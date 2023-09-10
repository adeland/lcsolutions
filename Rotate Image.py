class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        count = 0
        count1 = len(matrix) - 1
        while count1 > count:
            matrix[count], matrix[count1] = matrix[count1], matrix[count]
            count += 1
            count1 -= 1
        for i in range(len(matrix)):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
