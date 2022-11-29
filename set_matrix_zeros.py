class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        # look for rows
        height = len(matrix)
        width = len(matrix[0])
        
        cols =[]
        rows =[]
        # find colls and rows
        for r in range(height):
            for c in range(width):
                if matrix[r][c]== 0:
                    if r not in rows:
                        rows.append(r)
                    if c not in cols:
                        cols.append(c)
        
        for r in range(height):
            if r in rows:
                for i in range(width):
                    matrix[r][i] = 0
        
        for c in range(width):
            if c in cols:
                for j in range(height):
                    matrix[j][c] = 0
                    
        
        print(rows,cols)
        
        
        # look for colums
        
        return matrix
        


obj = Solution()

matrix = [[1,1,1],[1,0,1],[1,1,1]]
matrix1 = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]

print(obj.setZeroes(matrix1))