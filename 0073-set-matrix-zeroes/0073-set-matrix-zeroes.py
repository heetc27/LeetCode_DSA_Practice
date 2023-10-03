class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        rows = [1]*len(matrix)
        columns = [1]*len(matrix[0])
        a = []
        b = []
        for i in range(len(rows)):
            for j in range(len(columns)):
                if matrix[i][j]==0:
                    rows[i] = 0
                    columns[j] = 0
        for i in range(len(rows)):
            for j in range(len(columns)):
                if rows[i] == 0 or columns[j] == 0:
                    matrix[i][j] = 0
                
                    


                    