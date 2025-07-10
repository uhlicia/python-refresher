import numpy as np
import math

def sum_of_vectors(a,b):
    return a+b

def diff_of_vectors(a,b):
    return a-b

def sum_of_matrices(a,b):
    return a+b

def diff_of_matrices(a,b):
    return a-b

def dot_of_vectors(a,b):
    return np.dot(a,b)

def prod_of_matrices(a,b):
    return np.dot(a,b)

def magnitude_of_vector(a):
    sum = 0
    for x in a:
        sum += x**2
    return math.sqrt(sum)

def transpose(a):
    return a.T

    


