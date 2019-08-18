class Matrix:

    def __init__(self, width, height, data):
        if width == 0 or height == 0:
            raise ValueError

        self.width = width
        self.height = height
        self.data = data

    # Method for multiplication of two matrices.
    def __mul__(self, matrix):
        res = Matrix(matrix.width, self.height, list())
        for i in range(self.height):
            tmp = []
            for k in range(matrix.width):
                sum = 0
                for j in range(self.width):
                    sum += self.data[i][j] * matrix.data[j][k]
                tmp.append(sum)
            res.data.append(tmp)
        return res

    # Method for printing the result in specific format.
    def print_mat(self):
        for row in self.data:
            for num in row:
                print(num, end=' ')
            print('')


