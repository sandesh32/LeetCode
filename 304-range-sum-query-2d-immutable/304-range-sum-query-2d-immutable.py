class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix=matrix
        self.sumregion = []
        for i in range(len(matrix)+1):
            temp=[]
            for j in range(len(matrix[0])+1):
                temp.append(0)
            self.sumregion.append(temp)
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                self.sumregion[i+1][j+1]=self.sumregion[i+1][j]+self.sumregion[i][j+1]-self.sumregion[i][j]+matrix[i][j]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.sumregion[row2+1][col2+1]-self.sumregion[row1][col2+1]-self.sumregion[row2+1][col1]+self.sumregion[row1][col1]


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)