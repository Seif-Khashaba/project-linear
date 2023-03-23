from MATRIX import *
from seif_functions import *
from Functions import *
from MatrixOperationFunctions import *


# This function convert the matrix to it's orginal size if it was converted to square matrix
# it takes the matrix, number of rows and number of columns; however, it return nothing but it modifies the main matrix
def toSqrMat(mat, rowSize, colSize):
    if rowSize > colSize:
        for i in range(rowSize):
            for j in range(abs(colSize - rowSize)):
                mat[i].append(0)

    elif rowSize < colSize:
        for j in range(abs(colSize - rowSize)):
            mat.append(([0] * colSize))


# This function converts the matrix to square matrix if it wasn't
# it takes the matrix, number of rows and number of columns; however, it return nothing but it modifies the main matrix
def toOrginalMat(mat, rowSize, colSize):
    if rowSize < colSize:
        for j in range((abs(colSize - rowSize))):
            mat.pop()

    elif rowSize > colSize:
        for i in range(rowSize):
            for j in range((abs(colSize - rowSize))):
                mat[i].pop()


# this code re-arrange the matrix to prepare it for gauss elimination
def arrangeMat(LHS, RHS=0):
    for k in range(len(LHS)):
        for i in range(len(LHS)):
            for j in range(i + 1, len(LHS)):
                if LHS[j][i] != 0 and LHS[j - 1][i] == 0:
                    LHS[j], LHS[j - 1] = LHS[j - 1], LHS[j]
                    if RHS != 0:
                        RHS[j], RHS[j - 1] = RHS[j - 1], RHS[j]


# this function takes the matrix and row number and return the pivot and it's index if it exists
def getPivots(myPivots, mat, row_num):
    for index in range(len(mat[row_num])):
        if mat[row_num][index] != 0:
            pivot = mat[row_num][index]
            myPivots.append([pivot, index])
            return pivot, index


# this function implement gauss elimination algorithm
def gauss(myPivots, mat, matRHS=0):
    for i in range(len(mat)):

        myPivot = getPivots(myPivots, mat, i)
        if myPivot == None:
            continue
        for k in range(i, len(mat) - 1):
            myMultiplier = mat[k + 1][myPivot[1]] / (-myPivot[0])
            # This is for dubug only
            # print("multiplier:", myMultiplier, "pivot",
            #       myPivot[0], "index", myPivot[1])
            for j in range(len(mat)):
                mat[k + 1][j] = float("%f" %
                                      (myMultiplier * mat[i][j] + mat[k + 1][j]))
            if matRHS != 0:
                matRHS[k + 1][0] = float("%f" %
                                         (myMultiplier * matRHS[i][0] + matRHS[k + 1][0]))


# this function gets the Augmented part of the matrix
def isAugmented(rowSize):
    # input validation (input must be 0 or 1, 0 for no and 1 for yes)
    while True:
        try:
            isAug = int(input(
                "Does the Right Hand Side is exists?\nEnter 1 for YES or 0 for NO:"))
            if isAug == 1 or isAug == 0:
                break
            else:
                print("Invalid integar. Please enter 1 for YES or 0 for NO:")
        except ValueError:
            print("Invalid Input. Please enter a valid integer (1 or 0)")
    # if input is 1, this block of code will ask user for input and save these input in list
    if isAug:
        matRHS = createVector(rowSize)
        matRHS = [[i] for i in matRHS]
        return matRHS
    # if input is 0, this block of code will return 0
    else:
        return 0


# this function prints the results of echelon form function
def printResults(resLHS, resRHS, myPivots):
    print("= Row Echelon Form ===============================")
    for i in range(len(resLHS)):
        print("=", end=" ")
        for j in resLHS[i]:
            print("%-10f" % j, end=" ")
        if resRHS != 0:
            print("|", end=" ")
            for j in resRHS[i]:
                print("%-10f" % j, end=" ")
        print()
    print("==================================================")
    print("Number of Pivots:", len(myPivots), "       ", "Pivots :", myPivots)
    print("==================================================")


def linearComp(showInfo=1, printRes=1):
    if showInfo:
        print("Description: linear combination is the process of obtaining vector by adding two or more vectors (with "
              "different directions) which are multiplied by scalar values.")
        print("Formula: u = c₁.v₁ + c₂.v₂ + .... + cₙ.Vₙ (Where V is matrix of n colmns, cₙ is the scalar value and u "
              "is the vector obtained from the linear combination)")
    matRows, matCols = getMatrixSize()
    matLHS = createMatrix(matRows, matCols)
    matLHS = MATRIX(matLHS).matrix
    print("Enter u vector:")
    matRHS = createVector(matRows)
    matRHS = [[i] for i in matRHS]
    solutions = solve_matrix(matLHS, matRHS)  # seif's ref function
    # checks if there is any solution
    if any(solutions):
        if printRes:
            for i in range(len(matLHS)):
                print("{} × {}".format(solutions[i], matLHS[i]), end="")
                if i != len(matLHS) - 1:
                    print(" + ", end="")
        return 1
    else:
        return 0


def isDependent(showInfo=1, printRes=1):
    if showInfo:
        print("Description: This function check the relation between the columns of the matrix whether it's linearly "
              "dependent or not by using linear combination, If no such linear combination exists, then the vectors "
              "are said to be linearly independent.")
    rows, cols = getMatrixSize()
    while rows != cols:
        print(f"{bcolors.FAIL}Matrix should be square{bcolors.ENDC}")
        rows, cols = getMatrixSize()
    matrix = createMatrix(rows, cols)
    if determinant(matrix) == 0:
        if printRes:
            print("the system of linear equations is linearly dependent.")
        return 1
    else:
        if printRes:
            print("the system of linear equations is linearly independent.")
        return 0