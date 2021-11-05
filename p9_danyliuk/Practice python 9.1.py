import numpy as np
import itertools

def finish():
    repeat = input('To exit, enter \'mi scusi\' in the input field: ')
    if repeat == "mi scusi":
        print("The work is completed")
        
def random_matrix(dim):
    """
    The function generates dim x dim array of integers
    between 0 and 10.
    """
    matrix = np.random.randint(10, size = (dim, dim))
    return matrix

def permutations(matrix):
    """
    The function generates list of possible permutations 
    for a given matrix.
    """
    t = list(itertools.permutations(range(len(matrix))))
    return t

def permutation_multiplication(matrix, permutation):
    """
    The function generates a multiplication of permutation.
    """
    multiplication = 1
    for i in range(len(permutation)):
        multiplication *= matrix[i][permutation[i]]
    return multiplication

def determinant(matrix):
    """
    The function generates a sum of all members of determinant.
    """
    determinant = 0
    permutations_amount = 0
    for permutation in permutations(matrix):
        for i in permutation:
            for j in permutation:
                if i < j and permutation.index(i) > permutation.index(j):
                    permutations_amount += 1
        sign = (-1)**permutations_amount
        determinant += sign * permutation_multiplication(matrix, permutation)
    return determinant

while True:
    try:
        dim = int(input("Enter a size of matrix: "))
        if dim == 0:
            print("You have to enter an integer number! Except zero!")
            break
        else:
            matrix = random_matrix(dim)
            print("Printing matrix:", *matrix, sep = "\n")
            print("-" * 30)
            print("Determinant of matrix:", determinant(matrix))
            break
    except ValueError:
        print("You have to enter an integer number!")
        break
finish()
