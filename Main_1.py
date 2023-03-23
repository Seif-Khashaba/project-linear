from Func1 import *


# This function gets the echelon form of the matrix by using gauss elimination
def echelon():
    print("Left Hand Side...")
    matRows, matCols = getMatrixSize()  # get the size of the matrix
    matLHS = createMatrix(matRows, matCols)  # get the coffecent matrix
    matLHS = MATRIX(matLHS).matrix
    matRHS = isAugmented(matRows)  # get the Augmented part of the matrix
    myPivots = []  # this list to store pivots values and their index

    # Convert the matrix to square matrix if it wasn't
    toSqrMat(matLHS, len(matLHS), len(matLHS[0]))

    # re-arrange the matrix to prepare it for gauss elimination
    arrangeMat(matLHS, matRHS)
    # arrangeMat(matLHS, matRHS)

    # This is for dubug only
    print("our new matrix", matLHS)

    # applying gauss elimination
    gauss(myPivots, matLHS, matRHS)

    # Convert the matrix to it's original size if it was converted to square matrix
    toOrginalMat(matLHS, matRows, matCols)

    # Return the coffecent matrix, augmented matrix and the pivots
    return matLHS, matRHS, myPivots


# resLHS, resRHS, pivotsList = echelon()
# printResults(resLHS, resRHS, pivotsList)

# isDependent()