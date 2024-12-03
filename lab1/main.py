import numpy as np
import random

class Qubit:
    def __init__(self, a0, a1):
        self.a0 = a0
        self.a1 = a1
        self.matrix_as_vector = np.array([a0, a1])
        self.hadamard_matrix = np.array([[1, 1], [1, -1]]) / np.sqrt(2)
        self.matrix_as_vector_new_base = np.dot(self.hadamard_matrix, self.matrix_as_vector)
        
        print(f'Inputed {self.a0} and {self.a1} as \'a0\' and \'a1\'\nFormed matrix as vector: {self.matrix_as_vector}\n')
        print(f'Formed Hadamard matrix: \n{self.hadamard_matrix}\n')
        print(f'Formed matrix vector new base:\n{self.matrix_as_vector_new_base}\n')

    def measuring_standard(self):
        outcomes = [0, 1]
        probabilities = [abs(self.a0) ** 2, abs(self.a1) ** 2]
        res = random.choices(outcomes, probabilities)[0]
        print(f'Result of measuring in standard basis: |{res}>')
        return res

    def measuring_new_standard(self):
        outcomes = [0, 1]
        probabilities = [abs(self.matrix_as_vector_new_base[0]) ** 2, abs(self.matrix_as_vector_new_base[1]) ** 2]
        res = random.choices(outcomes, probabilities)[0]
        print(f'Result of measuring in standard basis: |{res}>')
        return res


q = Qubit(0.3, 0.7)
q.measuring_standard()
q.measuring_new_standard()