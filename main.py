def check_solved(c, A, b):
    for i in range(len(c)):
        if c[i] < 0:
            return False  
    return True

def simplex_step(c, A, b, solution, eps, Matrix):
    # find pivot
    pivot = None
    min_for_pivot = 10**100
    for i in range(len(c)):
        if c[i] < 0 and c[i] < min_for_pivot :
            min_for_pivot = c[i]
            pivot = i
    if pivot is None:   # solved already
        return c, A, b, solution, Matrix, True
    min_ratio = None
    row = None
    for i in range(len(A)):
        if(A[i][pivot] == 0):
            ratio = 10**100
        else:
            ratio = b[i] / A[i][pivot]
            if (min_ratio is None or ratio < min_ratio) and ratio > 0:  # find the minimum ratio
                min_ratio = ratio
                row = i
    # update the matrix
    if min_ratio is None: # check if solvable
        return c, A, b,solution, Matrix, False
    divider = A[row][pivot] #save our value 
    b[row] = b[row] / divider # normalize the pivot row
    for i in range(len(A[row])):
        A[row][i] = A[row][i] / divider
    for i in range(len(A)):
        if i != row:
            if A[i][pivot] != 0:    # update the other rows
                fact = A[row][pivot]  / A [i][pivot]
                b[i] -=  b[row]/fact
                for j in range(len(A[i])):
                    A[i][j] -=  A[row][j]/fact
    # update the vector
    c_factor = c[pivot] / A[row][pivot]
    for i in range(len(c)):
        c[i] -= c_factor * A[row][i]
        
    solution -= c_factor * b[row]
    Matrix[pivot] = row
    return c, A, b,solution, Matrix, True
    

def simplex_method(c, A, b, epsilon, maximize=True):
    solution = 0
    Matrix = [None for i in range(len(c))]
    ifSolvable = True
    checkForAccuracy = 0
    if maximize:
        c = [-i for i in c]
    while not check_solved(c, A, b):
        if ifSolvable is False: # check if unbounded
            return c, A, b, solution, Matrix, ifSolvable
        c, A, b, solution, Matrix, ifSolvable = simplex_step(c, A, b,solution, epsilon, Matrix)
        if abs(checkForAccuracy - solution) <= epsilon:
            if(not maximize):
                solution *= -1 # check for accuracy
            for i in range(len(Matrix)):
                if(Matrix[i] is None):
                    Matrix[i] = 0
                else:
                    Matrix[i] = b[Matrix[i]]    
            return c, A, b, solution, Matrix, ifSolvable
        checkForAccuracy = solution
    for i in range(len(Matrix)):
        if(Matrix[i] is None):
            Matrix[i] = 0
        else:
            Matrix[i] = b[Matrix[i]]
    if(not maximize):
                solution *= -1            
    return c, A, b, solution, Matrix, ifSolvable


def main():
    # Vector of coefficients of the objective function
    c = [float(i) for i in input("Vector of coefficients of the objective function: ").split()]
    # Matrix of coefficients of the constraints
    A = []
    while True:
        row_input = input("Row of matrix of the coefficients: ")
        if row_input == "":
            break
        row = list(map(float, row_input.split()))
        A.append(row)
    # Vector of coefficients of the right-hand side of the constraints  
    b = [float(i) for i in input("Vector of coefficients of the right-hand side of the constraints: ").split()]
    # Maximization problem
    maximize = input("max/min: ") == "max"
    # The approximation accuracy
    epsilon  = float(input("The approximation accuracy: "))
    c, A, b, solution, Matrix, ifSolvable = simplex_method(c, A, b, epsilon, maximize)
    if(ifSolvable):
        print("Optimal solution:")
        print(solution)
        print(Matrix)
    else:
        print("Unbounded solution")    
        
if __name__ == "__main__":
    main()
    
