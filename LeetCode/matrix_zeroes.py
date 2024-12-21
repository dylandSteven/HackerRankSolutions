from typing import List
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    for k in range(len(matrix)):
                        if matrix[k][j] != 0:
                            matrix[k][j] = 'x'
                    for l in range(len(matrix[i])):
                        if matrix[i][l] != 0:
                            matrix[i][l] = 'x'
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 'x' or matrix[i][j] == 0:
                    matrix[i][j] = 0

solution = Solution() 
solution.setZeroes([[1,1,1],[1,0,1],[1,1,1]])