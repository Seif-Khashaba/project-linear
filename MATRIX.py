# import all necessary libraries
from multipledispatch import dispatch
import pandas as pd


class MATRIX:
    def __init__(self, matrix):
        self.matrix = matrix  # making a matrix data member for every instance of the class
        self.matrix_op = [[0 for _ in range(len(matrix[0]))] for row in range(len(matrix))]  # Zero Matrix

    def Transpose(self):
        # This function is created to get the matrix transpose
        t_matrix = [[0 for x in range(len(self.matrix))] for y in range(len(self.matrix[0]))]
        for row in range(len(t_matrix)):  # looping through the matrix rows
            for element in range(len(self.matrix)):  # looping thorough the matrix cols
                t_matrix[row][element] = self.matrix[element][row]  # swapping rows with columns
        return MATRIX(t_matrix)

    def Replacement(self, pivot_row, row, scaler):
        # This function is responsible for making the matrix replacement operation
        self.matrix[row] = [(self.matrix[pivot_row][i] * scaler) + self.matrix[row][i] \
                            for i in range(len(self.matrix[pivot_row]))]
        return MATRIX(self.matrix)

    def Interchange(self, row_1, row_2):
        # This function is responsible for making the matrix Interchange operation
        self.matrix[row_1], self.matrix[row_2] = self.matrix[row_2], self.matrix[row_1]  # Swapping rows
        return MATRIX(self.matrix)

    def mul_row(self, row, scaler):
        # This function is used to multiply a certain row bt a certain scaler
        self.matrix[row] = [(i * scaler) for i in self.matrix[row]]
        return MATRIX(self.matrix)

    def Inverse(self):
        identity = [[0 for x in range(len(self.matrix))] for y in range(len(self.matrix[0]))]
        for i in range(len(identity)):
            identity[i][i] = 1
        for i in range(len(self.matrix)):
            if self.matrix[i][i] == 0:
                for j in range(i + 1, len(self.matrix)):
                    if self.matrix[j][i] != 0:
                        self.matrix = self.Interchange(i, j).matrix
                        identity = self.Interchange(i, j).matrix
                        break
            for j in range(len(self.matrix)):
                if j != i:
                    scaler = self.matrix[j][i] / self.matrix[i][i]
                    self.matrix = self.Replacement(i, j, -scaler).matrix
                    identity = self.Replacement(i, j, -scaler).matrix
        for i in range(len(self.matrix)):
            scaler = 1 / self.matrix[i][i]
            self.matrix = self.mul_row(i, scaler).matrix
            identity = self.mul_row(i, scaler).matrix
        return MATRIX(identity)

    def __str__(self):
        # This method is used to make the matrix ready to print and be Flexable
        df = pd.DataFrame(self.matrix)
        left, right = df.align(df, join="outer", axis=0)
        df = left.to_string(index=False, header=False)
        return df

    def __len__(self):
        # This method is used to return the size of a matrix
        return len(self.matrix), len(self.matrix[0])

    def __add__(self, other):
        # This method is used to add two matrices
        for row in range(len(self.matrix)):
            for element in range(len(self.matrix[0])):
                self.matrix_op[row][element] = self.matrix[row][element] + other.matrix[row][element]
        return MATRIX(self.matrix_op)

    def __sub__(self, other):
        # This method is used to subtract two matrices
        for row in range(len(self.matrix)):
            for element in range(len(self.matrix[0])):
                self.matrix_op[row][element] = self.matrix[row][element] - other.matrix[row][element]
        return MATRIX(self.matrix_op)

    @dispatch(float)
    def __mul__(self, scaler):
        # This method is used to scale a matrix
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[0])):
                self.matrix_op[i][j] = self.matrix[i][j] * scaler
        return MATRIX(self.matrix_op)

    @dispatch(object)
    def __mul__(self, other):
        # This method is used to multiply two matrices
        if len(self.matrix[0]) == len(other.matrix):
            matrix_mul = [[0 for x in range(len(other.matrix[0]))] for y in range(len(self.matrix))]
            for i in range(len(self.matrix)):
                for j in range(len(other.matrix[0])):
                    for k in range(len(other.matrix)):
                        matrix_mul[i][j] += self.matrix[i][k] * other.matrix[k][j]
            return MATRIX(matrix_mul)
        else:
            print("The two matrices cannot be multiplied")