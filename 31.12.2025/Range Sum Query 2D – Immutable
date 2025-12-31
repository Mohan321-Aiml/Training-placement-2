class NumMatrix:
    def __init__(self, matrix):
        if not matrix:
            self.p=[]
            return
        m,n=len(matrix),len(matrix[0])
        self.p=[[0]*(n+1) for _ in range(m+1)]
        for i in range(m):
            for j in range(n):
                self.p[i+1][j+1]=matrix[i][j]+self.p[i][j+1]+self.p[i+1][j]-self.p[i][j]
    def sumRegion(self, r1, c1, r2, c2):
        return self.p[r2+1][c2+1]-self.p[r1][c2+1]-self.p[r2+1][c1]+self.p[r1][c1]
