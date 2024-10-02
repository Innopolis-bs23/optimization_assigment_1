def check_solved(c, A, b):
    for i in range(len(c)):
        if c[i] < 0:
            return False
    for i in range(len(A)):
        if A[i][0] < 0:
            return False
    return True

def simplex_step(c, A, b):
    # find pivot
    pivot = None
    for i in range(len(c)):
        if c[i] < 0:
            pivot = i
            break
    if pivot is None:   # solved already
        return c, A, b
    min_ratio = None
    for i in range(len(A)):
        if A[i][pivot] > 0:
            ratio = b[i] / A[i][pivot]
            if min_ratio is None or ratio < min_ratio:  # find the minimum ratio
                min_ratio = ratio
                row = i
    # update the matrix
    b[row] /= A[row][pivot] # normalize the pivot row
    for i in range(len(A[row])):
        A[row][i] /= A[row][pivot]
    for i in range(len(A)):
        if i != row:    # update the other rows
            fact = A[i][pivot]
            b[i] -= fact * b[row]
            for j in range(len(A[i])):
                A[i][j] -= fact * A[row][j]
    # update the vector
    c_factor = c[pivot]
    for i in range(len(c)):
        c[i] -= c_factor * A[row][i]
    return c, A, b
    

def simplex_method(c, A, b, epsilon, maximize=True):
    if not maximize:
        c = [-i for i in c]
    while not check_solved(c, A, b):
        c, A, b = simplex_step(c, A, b)
    return c, A, b


def main():
    # Vector of coefficients of the objective function
    c = [float(i) for i in input("Vector of coefficients of the objective function: ").split()]
    # Matrix of coefficients of the constraints
    A = [[float(i) for i in input("Matrix of coefficients of the constraints: ").split()] for _ in range(2)]
    # Vector of coefficients of the right-hand side of the constraints
    b = [float(i) for i in input("Vector of coefficients of the right-hand side of the constraints: ").split()]
    # Maximization problem
    maximize = input("max/min: ") == "max"
    # The approximation accuracy
    epsilon  = float(input("The approximation accuracy: "))
    c, A, b = simplex_method(c, A, b, epsilon, maximize)
    print("Optimal solution:")
    print(c)
    print(A)
    print(b)
        
if __name__ == "__main__":
    main()