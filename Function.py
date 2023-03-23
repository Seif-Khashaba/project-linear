import numpy as np
from pylatex import Document, Section, Subsection, Tabular, Math, TikZ, Axis, \
    Plot, Figure, Matrix, Alignat
from pylatex.utils import italic
import os


class ColError(Exception):
    pass


class FormatError(Exception):
    pass


class RangeError(Exception):
    pass


class ElementError(Exception):
    pass


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def ValidateMatrixElement(element):
    if not element.lstrip("-").isdigit():
        raise ElementError
    return int(element)


def getMatrixSize():
    print(f"{bcolors.FAIL}{bcolors.UNDERLINE}ONLY {bcolors.WARNING}Matrices to size 5x5 are allowed...{bcolors.ENDC}")
    while True:
        try:
            size = input(f"Please enter matrix size in format {bcolors.WARNING}(number of rows and number of columns "
                         f"separated with "
                         f"english letter 'x'){bcolors.ENDC} i.e (3x3): ")
            if not ("x" in size) or len(size) != 3:
                raise FormatError
            else:
                size = size.split('x')
                size = [int(i) for i in size]
                if 1 <= size[0] <= 5 and 1 <= size[1] <= 5:
                    rows, cols = size[0], size[1]
                    break
                else:
                    raise RangeError
        except FormatError:
            print(f"{bcolors.FAIL}Size is in the wrong format...{bcolors.ENDC}")
            print(f"{bcolors.WARNING}The right format is [MxN] Where M and N are positive integers separated with "
                  f"english letter 'x' {bcolors.ENDC}\n")
        except RangeError:
            print(f"{bcolors.FAIL}ONLY Matrices to size 5x5 are allowed{bcolors.ENDC}")
            print(f"{bcolors.WARNING}please Enter a valid size{bcolors.ENDC}\n")
    return rows, cols


def createMatrix(rows, cols):
    print(f"{bcolors.UNDERLINE}{bcolors.WARNING}Enter row by row, numbers separated with one space "
          f"{bcolors.OKBLUE}i.e(1 2 3){bcolors.ENDC}")
    matrix = []
    n_rows = 1
    while True:
        try:
            while len(matrix) != rows:
                row = input(f"Enter row [{bcolors.OKCYAN}{n_rows}{bcolors.ENDC}]: ")
                if row.count(' ') == len(row.split(' ')) - 1:
                    row = row.split(' ')
                    row = [ValidateMatrixElement(i) for i in row]
                    if len(row) == cols:
                        matrix.append(row)
                        n_rows += 1
                    else:
                        raise RangeError
                else:
                    raise FormatError
            break
        except FormatError:
            print(f"{bcolors.FAIL}{bcolors.UNDERLINE}The row numbers are in a wrong format...{bcolors.ENDC}")
            print(f"{bcolors.OKGREEN}the right format is MxN Where M and N are integers{bcolors.OKBLUE} i.e(1 2 3)."
                  f"{bcolors.ENDC}")
        except RangeError:
            print("number of element in the row is not true")
        except ElementError:
            print(f"\t{bcolors.FAIL}[-] NOT a valid input")
            print(f"\t{bcolors.OKGREEN}[+] valid inputs are integers only..{bcolors.ENDC}")
    return matrix


def createVector(original_matrix_rows):
    vector = []
    while len(vector) != original_matrix_rows:
        try:
            element = float(input(f"Enter element [{bcolors.OKCYAN}{len(vector) + 1}{bcolors.ENDC}]: "))
            vector.append(element)
        except ValueError:
            print(f"\t{bcolors.FAIL}[-] NOT a valid input")
            print(f"\t{bcolors.OKGREEN}[+] valid inputs are integers only..{bcolors.ENDC}")
    return vector


def validateWithRange(n1, n2, message):
    while True:
        try:
            number = int(input(message))
            if n1 <= number <= n2:
                break
            else:
                raise ValueError
        except ValueError:
            print(f"\t{bcolors.FAIL}[-] NOT a valid input")
            print(f"\t{bcolors.OKGREEN}[+] valid inputs are integers {n1}~{n2}..{bcolors.ENDC}")
    return number


def createLatexFile():
    geometry_options = {"tmargin": "1cm", "lmargin": "10cm"}
    doc = Document(geometry_options=geometry_options)

    with doc.create(Section('The simple stuff')):
        doc.append('Some regular text and some')
        doc.append(italic('italic text. '))
        doc.append('\nAlso some crazy characters: $&#{}')
        with doc.create(Subsection('Math that is incorrect')):
            doc.append(Math(data=['2*3', '=', 9]))
    doc.generate_pdf('full', clean_tex=False)