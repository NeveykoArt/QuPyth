import numpy as np
import math

# Функция умножения матрицы на вектор с коэффициентом
def matrix_vector_multiplication(A, v, k_A=1, k_v=1):
    if len(A[0]) != len(v):
        raise ValueError("Число столбцов матрицы должно быть равно размеру вектора.")
    result = [0 for _ in range(len(A))]
    for i in range(len(A)):
        for j in range(len(v)):
            result[i] += k_A * A[i][j] * k_v * v[j]
    return result

# Функция перевода вектора в скобочную нотацию для произвольного числа состояний с коэффициентом
def vector_to_bracket_notation(v, k=1):
    if len(v) == 2:
        return f"{k * v[0]:.2f}|0⟩ + {k * v[1]:.2f}|1⟩"
    else:
        n = len(v)
        num_qubits = (n - 1).bit_length()  # Определяем количество кубитов
        notation = " + ".join(f"{k * k_v:.2f}|{format(i, f'0{num_qubits}b')}⟩" for i, k_v in enumerate(v) if k * k_v != 0)
        return notation

def build_F(bool_func, n):
    size_matrix = 2 ** n
    F = np.zeros((size_matrix, size_matrix), dtype=int)
    
    for elem_x in bool_func:
        x = ''
        for item in elem_x[0]:
            x = x + str(item)
        for i in range(0, 2 ** (len(elem_x[1]))):
            y = bin(i)[2:].zfill(len(elem_x[1]))
            poz_row = x + y
            f = ''
            for j in range(0, len(y)):
                f = f + str(int(y[j]) ^ elem_x[1][j])
            poz_col = x + f
            F[int(poz_row, 2)][int(poz_col, 2)] = 1
    return F

truth_table_test1 = [
    ([0, 0], [1]),
    ([0, 1], [1]),
    ([1, 0], [0]),
    ([1, 1], [1])
]

#zadanie 2
truth_table_task2 = [
([0, 0, 0, 0], [0, 0, 0, 1]),
([0, 0, 0, 1], [0, 1, 0, 0]),
([0, 0, 1, 0], [0, 0, 0, 1]),
([0, 0, 1, 1], [0, 1, 0, 0]),
([0, 1, 0, 0], [0, 0, 0, 1]),
([0, 1, 0, 1], [0, 1, 0, 0]),
([0, 1, 1, 0], [0, 0, 0, 1]),
([0, 1, 1, 1], [0, 1, 0, 0]),
([1, 0, 0, 0], [0, 0, 0, 1]),
([1, 0, 0, 1], [0, 1, 0, 0]),
([1, 0, 1, 0], [0, 0, 0, 1]),
([1, 0, 1, 1], [0, 1, 0, 0]),
([1, 1, 0, 0], [0, 0, 0, 1]),
([1, 1, 0, 1], [0, 1, 0, 0]),
([1, 1, 1, 0], [0, 0, 0, 1])
]

register = [0, 0, 1, 0, 0, 0, 0, 0] #00100000

F_1 = build_F(truth_table_test1, 3)
print(vector_to_bracket_notation(matrix_vector_multiplication(F_1, register)))

# print(build_F(truth_table_test1, 3))
# print(build_F(truth_table_test2, 4))

def generate_binary_table(a, m):
    num_bits = math.ceil(math.log2(m))  # Количество бит

    print("[")
    for x in range(m):
        fx = (a ** x) % m
        x_bits = f"{x:0{num_bits}b}"
        f_bits = f"{fx:0{num_bits}b}"
        print("".join('(' + '[' + ", ".join(x_bits) + '], '+ '[' + ", ".join(f_bits) + ']' + '),'))
    print("]")

m = 15

print(generate_binary_table(4, m))

F_2 = build_F(truth_table_task2, 8)

for i in range(m):
    num_bits = math.ceil(math.log2(m))
    num_states = 2 ** (2 * num_bits)

    initial_state = np.zeros(num_states, dtype=int)
    initial_index = int(f"{i:0{num_bits}b}{"0" * num_bits}", 2)
    initial_state[initial_index] = 1
    print(vector_to_bracket_notation(matrix_vector_multiplication(F_2, initial_state)))