import pytest
from main import simplex_method

def check_float_equal(a, b, epsilon):
    return abs(a - b) <= epsilon

def check_lists_equal(a, b, epsilon):
    for i in range(min(len(a), len(b))):
        if not check_float_equal(a[i], b[i], epsilon):
            return False
    return True

def check_matrix_equal(a, b, epsilon):
    if len(a) != len(b):
        return False
    for i in range(len(a)):
        if not check_lists_equal(a[i], b[i], epsilon):
            return False
    return True

# Ex 1
def test_simplex_method1():
    c = [9, 10, 16, 0, 0, 0]
    A = [[18, 15, 12, 1, 0, 0], 
         [6, 4, 8, 0, 1, 0], 
         [5, 3, 3, 0, 0, 1]]
    b = [360, 192, 180]
    epsilon = 0.01
    maximize = True
    c, A, b, solution, X, _ = simplex_method(c, A, b, epsilon, maximize)
    
    assert check_float_equal(solution, 400, epsilon)
    assert check_matrix_equal(A, 
                              [[1, 1, 0, 1/9, -1/6, 0],
                              [3/4 - 1/2, 0, 1, -1/9/2, 1/8+1/6/2, 0],
                              [11/4-3/2, 0, 0, -3/9/2, -3/8+3/2/6, 1]],
                              epsilon) 
    assert  check_lists_equal(c, 
                              [5, 0, 0, 2/9, 5/3, 0],
                              epsilon)
    assert  check_lists_equal(b,
                              [8, 20, 96],
                              epsilon)
    assert  check_lists_equal(X,
                              [0, 8, 20],
                              epsilon)
    
# Ex 2
def test_simplex_method2():
    c = [-2, 2, -6, 0, 0, 0]
    A = [[2, 1, -2, 1, 0 ,0], 
         [1, 2, 4, 0, 1, 0], 
         [1, -1, 2, 0, 0, 1]]
    b = [24, 23, 10]
    epsilon = 0.01
    maximize = False
    c, A, b, solution, X, _ = simplex_method(c, A, b, epsilon, maximize)
    
    assert check_float_equal(solution, 
                             -123/4,
                             epsilon)
    assert check_matrix_equal(A, 
                              [[3, 0, 0, 1, 0, 1],
                              [-1/4, 1, 0, 0, 1/4, -1/2],
                              [3/8, 0, 1, 0, 1/8, 1/4]],
                              epsilon)
    assert check_lists_equal(c,
                             [3/4, 0, 0, 0, 1/4, 5/2],
                             epsilon)
    assert check_lists_equal(b,
                             [34, 3/4, 43/8], 
                             epsilon)
    assert check_lists_equal(X,
                             [0, 3/4, 43/8],
                             epsilon)


# Ex 3
def test_simplex_method3():
    c = [60, 70, 50, 0, 0, 0]
    A = [[2, 3, 1, 1, 0, 0], 
         [4, 2, 3, 0, 1, 0], 
         [1, 2, 4, 0, 0, 1]]
    b = [150, 300, 200]
    epsilon = 0.01
    maximize = True
    c, A, b, solution, X, _ = simplex_method(c, A, b, epsilon, maximize)
    
    assert check_float_equal(solution, 5017.241379310345, epsilon)
    assert  check_lists_equal(X,
                              [44.82758620689655, 8.620689655172416, 34.48275862068965],
                              epsilon)

# Ex 4
def test_simplex_method4():
    c = [3, 5, 2, 4, 0, 0]
    A = [[2, 3, 1, 2, 1, 0, 0], 
         [1, 2, 3, 1, 0, 1, 0], 
         [3, 1, 2, 4, 0, 0, 1]]
    b = [12, 10, 15]
    epsilon = 0.01
    maximize = True
    c, A, b, solution, X, _ = simplex_method(c, A, b, epsilon, maximize)
    
    assert check_float_equal(solution, 22.2, epsilon)
    assert  check_lists_equal(X,
                              [0, 1.8, 0, 3.3],
                              epsilon)

from math import log 
# Ex 5
def test_simplex_method5():
    c = [4, 3, 5, 2, 6, 0, 0, 0, 0]
    A = [[2, 3, 4, 1, 2, 1, 0, 0, 0], 
         [1, 2, 1, 3, 3, 0, 1, 0, 0], 
         [3, 1, 5, 2, 1, 0, 0, 1, 0],
         [4, 2, 3, 4, 5, 0, 0, 0, 1]]
    b = [30, 24, 36, 48]
    epsilon = 0.01
    maximize = True
    c, A, b, solution, X, _ = simplex_method(c, A, b, epsilon, maximize)
    
    assert check_float_equal(solution, 61.66, epsilon)
    assert  check_lists_equal(X,
                              [1.33, 0, 3.67, 0, 6.33],
                              epsilon)