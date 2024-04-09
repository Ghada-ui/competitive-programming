class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        zeros=[]
        for row in range(len(matrix)):
            for col in range (len(matrix[0])):
                if matrix[row][col] == 0:
                    zeros.append(row)
                    zeros.append(col)           
        for x in range(0,len(zeros)-1,2):     
            i = 0
            j = 0
            while i < len(matrix):
                matrix[i][zeros[x + 1]] = 0
                i += 1
            while j < len(matrix[0]):
                matrix[zeros[x]][j] = 0
                j += 1
                
        print(matrix)                