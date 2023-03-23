from MATRIX import *
from Functions import *
import math
import numpy as np


def addMatrices():
    rows, cols = getMatrixSize()
    print(f"\n\t{bcolors.UNDERLINE}{bcolors.WARNING}Enter first matrix{bcolors.ENDC}")
    matrix1 = createMatrix(rows, cols)
    print(f"\n\t{bcolors.UNDERLINE}{bcolors.WARNING}Enter second matrix{bcolors.ENDC}")
    matrix2 = createMatrix(rows, cols)
    matrix1 = MATRIX(matrix1)
    matrix2 = MATRIX(matrix2)
    matrix3 = matrix1 + matrix2
    print(f"\n{bcolors.OKCYAN}{bcolors.BOLD}The result is:{bcolors.ENDC}")
    print(matrix3)


def subtractMatrices():
    rows, cols = getMatrixSize()
    print(f"\t{bcolors.UNDERLINE}{bcolors.WARNING}Enter first matrix{bcolors.ENDC}")
    matrix1 = createMatrix(rows, cols)
    print(f"\t{bcolors.UNDERLINE}{bcolors.WARNING}Enter second matrix{bcolors.ENDC}")
    matrix2 = createMatrix(rows, cols)
    matrix1 = MATRIX(matrix1)
    matrix2 = MATRIX(matrix2)
    matrix3 = matrix1 - matrix2
    print(f"\n{bcolors.OKCYAN}{bcolors.BOLD}The result is:{bcolors.ENDC}")
    print(matrix3)


def multiplyMatrices():
    print(f"\n\t{bcolors.UNDERLINE}{bcolors.WARNING}Enter first matrix{bcolors.ENDC}")
    rows_1, cols_1 = getMatrixSize()
    matrix1 = createMatrix(rows_1, cols_1)
    print(f"\n\t{bcolors.UNDERLINE}{bcolors.WARNING}Enter second matrix{bcolors.ENDC}")
    rows_2, cols_2 = getMatrixSize()
    while cols_1 != rows_2:
        print(f"{bcolors.FAIL}The number of columns in the first matrix must be equal to the number of rows in the "
              f"second matrix{bcolors.ENDC}")
        rows_2, cols_2 = getMatrixSize()
    matrix2 = createMatrix(rows_2, cols_2)
    matrix1 = MATRIX(matrix1)
    matrix2 = MATRIX(matrix2)
    matrix3 = matrix1 * matrix2
    print(f"\n{bcolors.OKCYAN}{bcolors.BOLD}The result is:{bcolors.ENDC}")
    print(matrix3)


def scalarMultiplication():
    rows, cols = getMatrixSize()
    matrix = createMatrix(rows, cols)
    matrix = MATRIX(matrix)
    while True:
        try:
            scaler = float(input(f"{bcolors.WARNING}Enter the scaler: {bcolors.ENDC}"))
            break
        except ValueError:
            print(f"{bcolors.FAIL}Please, enter a valid scaler{bcolors.ENDC}")
    matrix *= scaler
    print(f"\n{bcolors.OKCYAN}{bcolors.BOLD}The result is:{bcolors.ENDC}")
    print(matrix)


def transposeMatrix():
    rows, cols = getMatrixSize()
    matrix = createMatrix(rows, cols)
    matrix = MATRIX(matrix)
    print(f"\n{bcolors.OKCYAN}{bcolors.BOLD}The result is:{bcolors.ENDC}")
    print(matrix.Transpose())


def inverseMatrix():
    rows, cols = getMatrixSize()
    while rows != cols:
        try:
            rows, cols = getMatrixSize()
            break
        except ValueError:
            print(f"{bcolors.FAIL}The matrix is not square{bcolors.ENDC}")
    matrix = createMatrix(rows, cols)
    matrix = MATRIX(matrix)
    print(f"\n{bcolors.OKCYAN}{bcolors.BOLD}The result is:{bcolors.ENDC}")
    print(matrix.Inverse())


def MatrixTransfromation():
    rows, cols = getMatrixSize()
    matrix = createMatrix(rows, cols)
    matrix = MATRIX(matrix)
    print(
        f"\t[{bcolors.OKCYAN}1{bcolors.ENDC}] scale\n\t[{bcolors.OKCYAN}2{bcolors.ENDC}] shift\n\t[{bcolors.OKCYAN}3{bcolors.ENDC}] shear x\n\t[{bcolors.OKCYAN}4{bcolors.ENDC}] shear y")
    choice = validateWithRange(1, 4,
                               f"{bcolors.WARNING}Enter the transformation operation you want to apply: {bcolors.ENDC}")
    if choice == 1:
        while True:
            try:
                xscaler = float(input(f"{bcolors.WARNING}Enter the x scaler: {bcolors.ENDC}"))
                break
            except ValueError:
                print(f"{bcolors.FAIL}Please, enter a valid scaler{bcolors.ENDC}")
        while True:
            try:
                yscaler = float(input(f"{bcolors.WARNING}Enter the y scaler: {bcolors.ENDC}"))
                break
            except ValueError:
                print(f"{bcolors.FAIL}Please, enter a valid scaler{bcolors.ENDC}")
        transformation_mat(xscaler, yscaler, choice)
    elif choice == 2:
        while True:
            try:
                xshift = float(input(f"{bcolors.WARNING}Enter the x shift: {bcolors.ENDC}"))
                break
            except ValueError:
                print(f"{bcolors.FAIL}Please, enter a valid shift{bcolors.ENDC}")
        while True:
            try:
                yshift = float(input(f"{bcolors.WARNING}Enter the y shift: {bcolors.ENDC}"))
                break
            except ValueError:
                print(f"{bcolors.FAIL}Please, enter a valid shift{bcolors.ENDC}")
        transformation_mat(xshift, yshift, choice)
    elif choice == 3:
        while True:
            try:
                xshear = float(input(f"{bcolors.WARNING}Enter the x shear: {bcolors.ENDC}"))
                break
            except ValueError:
                print(f"{bcolors.FAIL}Please, enter a valid shear{bcolors.ENDC}")
        transformation_mat(xshear, 1, choice)
    elif choice == 4:
        while True:
            try:
                yshear = float(input(f"{bcolors.WARNING}Enter the y shear: {bcolors.ENDC}"))
                break
            except ValueError:
                print(f"{bcolors.FAIL}Please, enter a valid shear{bcolors.ENDC}")
        transformation_mat(1, yshear, choice)


def matrixDeterminant():
    rows, cols = getMatrixSize()
    while rows != cols:
        try:
            rows, cols = getMatrixSize()
            break
        except ValueError:
            print(f"{bcolors.FAIL}The matrix is not square{bcolors.ENDC}")
    matrix = createMatrix(rows, cols)
    matrix = MATRIX(matrix)
    print(f"\n{bcolors.OKCYAN}{bcolors.BOLD}The result is:{bcolors.ENDC}")
    print(determinant(matrix.matrix))


def transformation_mat(x, y, c):
    if c == 1:
        transformation = [[x, 0, 0], [0, y, 0], [0, 0, 1]]
        print(MATRIX(transformation))
    if c == 2:
        transformation = [[1, 0, x], [0, 1, y], [0, 0, 1]]
        print(MATRIX(transformation))
    if c == 3:
        transformation = [[1, x, 0], [0, 1, 0], [0, 0, 1]]
        print(MATRIX(transformation))
    if c == 4:
        transformation = [[1, 0, 0], [y, 1, 0], [0, 0, 1]]
        print(MATRIX(transformation))


def get_submatrix(matrix, i, j):
    """Returns the submatrix of matrix by removing row i and column j."""
    return [row[:j] + row[j + 1:] for row in (matrix[:i] + matrix[i + 1:])]


def determinant(matrix):
    # matrix should be a list of lists
    if len(matrix) == 2 and len(matrix[0]) == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

    det = 0
    for i in range(len(matrix)):
        sign = (-1) ** i
        sub_matrix = get_submatrix(matrix, 0, i)
        det += sign * matrix[0][i] * determinant(sub_matrix)
    return det


def rotation(angle, axis):
    if axis == 'x':
        return np.array([[1, 0, 0],
                         [0, np.cos(angle), -np.sin(angle)],
                         [0, np.sin(angle), np.cos(angle)]])
    elif axis == 'y':
        return np.array([[np.cos(angle), 0, np.sin(angle)],
                         [0, 1, 0],
                         [-np.sin(angle), 0, np.cos(angle)]])
    elif axis == 'z':
        return np.array([[np.cos(angle), -np.sin(angle), 0],
                         [np.sin(angle), np.cos(angle), 0],
                         [0, 0, 1]])


def matrixRotation():
    while True:
        try:
            angle = float(input("Enter the angle: "))
            break
        except ValueError:
            print("Please, enter a valid angle")
    angle = (math.pi / 180) * angle
    while True:
        axis = input("Enter the axis: ")
        if axis == 'x' or axis == 'y' or axis == 'z':
            break
        else:
            print("Please, enter a valid axis")
    print(rotation(angle, axis))