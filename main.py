import os
from MatrixOperationFunctions import *
from Functions_1 import *
from Main_1 import *


def programIntro():
    os.system('cls')
    print(f"{bcolors.UNDERLINE}{bcolors.BOLD}Welcome to {bcolors.OKCYAN}[{bcolors.WARNING}Linear Algebra Solver"
          f"{bcolors.OKCYAN}]{bcolors.ENDC}{bcolors.UNDERLINE}{bcolors.BOLD} your tool for solving linear"
          f" systems{bcolors.ENDC}")
    print("Here some features we provide please choose...")
    print(f"\t[{bcolors.OKCYAN}1{bcolors.ENDC}] Matrix Operation\n\t[{bcolors.OKCYAN}2{bcolors.ENDC}] "
          f"System fo equations and Echelon form")
    choice = validateWithRange(1, 2, "please, enter your choice: ")
    if choice == 1:
        matrixOperation()
    else:
        solveSystem()


def matrixOperation():
    os.system('cls')
    print(f"Welcome to {bcolors.OKCYAN}[{bcolors.WARNING}Matrix Operation{bcolors.OKCYAN}]{bcolors.ENDC}")
    print("Please choose the operation you want to perform")
    print(
        f"\t[{bcolors.OKCYAN}1{bcolors.ENDC}] Add two matrices\n\t[{bcolors.OKCYAN}2{bcolors.ENDC}] Subtract two matrices")
    print(
        f"\t[{bcolors.OKCYAN}3{bcolors.ENDC}] Multiply two matrices\n\t[{bcolors.OKCYAN}4{bcolors.ENDC}] Scalar multiplication")
    print(
        f"\t[{bcolors.OKCYAN}5{bcolors.ENDC}] Transpose matrix\n\t[{bcolors.OKCYAN}6{bcolors.ENDC}] Matrix transformation")
    print(
        f"\t[{bcolors.OKCYAN}7{bcolors.ENDC}] Calculate a determinant\n\t[{bcolors.OKCYAN}8{bcolors.ENDC}] Matrx routeation")
    print(f"\t[{bcolors.OKCYAN}9{bcolors.ENDC}] Inverse a matrix\n")
    choice = validateWithRange(1, 9, "please, enter your choice: ")
    # call the function based on the choice
    if choice == 1:
        addMatrices()
    elif choice == 2:
        subtractMatrices()
    elif choice == 3:
        multiplyMatrices()
    elif choice == 4:
        scalarMultiplication()
    elif choice == 5:
        transposeMatrix()
    elif choice == 6:
        MatrixTransfromation()
    elif choice == 7:
        matrixDeterminant()
    elif choice == 8:
        matrixRotation()
    elif choice == 9:
        inverseMatrix()


def solveSystem():
    os.system('cls')
    print(
        f"Welcome to {bcolors.OKCYAN}[{bcolors.WARNING}System fo equations and Echelon form{bcolors.OKCYAN}]{bcolors.ENDC}")
    print("Please choose the operation you want to perform")
    print(
        f"\t[{bcolors.OKCYAN}1{bcolors.ENDC}] Echelon Form\n\t[{bcolors.OKCYAN}2{bcolors.ENDC}] Linear Combination ")
    print(f"\t[{bcolors.OKCYAN}3{bcolors.ENDC}] Dependency")
    choice = validateWithRange(1, 3, "please, enter your choice: ")
    # call the function based on the choice
    if choice == 1:
        echelonForm()
    elif choice == 2:
        LinearCombination()
    else:
        Dependency()


def echelonForm():
    resLHS, resRHS, pivotsList = echelon()
    printResults(resLHS, resRHS, pivotsList)


def LinearCombination():
    linearComp()


def Dependency():
    isDependent()


programIntro()