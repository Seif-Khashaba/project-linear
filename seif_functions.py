def solve_matrix(A, b):
    # Augment the matrix with the right-hand side
    AB = [[A[i][j] for j in range(len(A[i]))] + [b[i][0]] for i in range(len(A))]

    # Apply Gauss-Jordan elimination
    for pivot_row in range(len(AB)):
        # Check if the pivot element is zero
        if AB[pivot_row][pivot_row] == 0:
            # Find a row with a non-zero pivot element and swap it with the current row
            found_nonzero_pivot = False
            for row in range(pivot_row+1, len(AB)):
                if AB[row][pivot_row] != 0:
                    AB[pivot_row], AB[row] = AB[row], AB[pivot_row]
                    found_nonzero_pivot = True
                    break
            if not found_nonzero_pivot:
                # If no non-zero pivot element was found, try to find a non-zero element in the same column and divide it by the pivot element
                for row in range(pivot_row+1, len(AB)):
                    if AB[row][pivot_row] != 0:
                        factor = AB[row][pivot_row] / AB[pivot_row][pivot_row]
                        for j in range(len(AB[row])):
                            AB[row][j] -= factor * AB[pivot_row][j]
                        found_nonzero_pivot = True
                        break
                if not found_nonzero_pivot:
                    print("Matrix is singular")
                    # If no non-zero element was found in the same column, check if the right-hand side is zero
                    if all(b[i][0] == 0 for i in range(len(b))):
                        # If the right-hand side is zero, the system has an infinite number of solutions
                        print("Solution type : infinite solutions")
                        return list([0] * len(A[0]))
                    else:
                        # If the right-hand side is non-zero, the system has no solutions
                        print("Solution type : no solution (Contradiction)\nWe can't write vector u as a linear combination of the given vectors.")
                        return list([0] * len(A[0]))
        # Normalize the pivot row
        pivot = AB[pivot_row][pivot_row]
        for j in range(len(AB[pivot_row])):
            if AB[pivot_row][j]!= 0:
                AB[pivot_row][j] /= pivot

        # Eliminate the pivot variable from all other rows
        for row in range(len(AB)):
            if row != pivot_row:
                factor = AB[row][pivot_row]
                for j in range(len(AB[row])):
                    AB[row][j] -= factor * AB[pivot_row][j]

    # Separate the solutions (x) from the augmented matrix
    x = [AB[i][-1] for i in range(len(b))]

    return x
