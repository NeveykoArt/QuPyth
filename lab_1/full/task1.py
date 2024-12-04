# Функция печати матрицы
def print_matrix(matrix, name, k=1):
    print(f"{name} = {k} * [", end="")
    # Определение ширины для выравнивания
    max_len = max(len(f"{elem:6.2f}") for row in matrix for elem in row)
    for i, row in enumerate(matrix):
        if i > 0:
            print(" " * (len(name) + 8 + (2 if not isinstance(k, int) else 0)), end="")  # Выравнивание строк
        print("   ".join(f"{elem:{max_len}.2f}" for elem in row), end=" ")
        if i == len(matrix) - 1:
            print(" ]")  # Закрытие матрицы для последней строки
        else:
            print()
    print()

# Функция печати вектора
def print_vector(vector, name, k=1):
    # Печать заголовка и коэффициента
    print(f"{name} = {k} * [", "  ".join(f"{elem:.2f}" for elem in vector), "]\n")

# Функция умножения матриц с коэффициентами
def matrix_multiplication(A, B, k_A=1, k_B=1):
    if len(A[0]) != len(B):
        raise ValueError("Число столбцов матрицы A должно быть равно числу строк матрицы B.")
    result = [[0 for _ in range(len(B[0]))] for _ in range(len(A))]
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                result[i][j] += k_A * A[i][k] * k_B * B[k][j]
    return result

# Функция умножения матрицы на вектор с коэффициентом
def matrix_vector_multiplication(A, v, k_A=1, k_v=1):
    if len(A[0]) != len(v):
        raise ValueError("Число столбцов матрицы должно быть равно размеру вектора.")
    result = [0 for _ in range(len(A))]
    for i in range(len(A)):
        for j in range(len(v)):
            result[i] += k_A * A[i][j] * k_v * v[j]
    return result

# Функция тензорного произведения матриц с коэффициентами
def tensor_product_matrixes(A, B, k_A=1, k_B=1):
    result = []
    for i in range(len(A)):
        for j in range(len(B)):
            row = []
            for k in range(len(A[0])):
                for l in range(len(B[0])):
                    row.append(k_A * A[i][k] * k_B * B[j][l])
            result.append(row)
    return result

# Функция тензорного произведения векторов с коэффициентами
def tensor_product_vectors(v, w, k_v=1, k_w=1):
    result = []
    for i in range(len(v)):
        for j in range(len(w)):
            result.append(k_v * v[i] * k_w * w[j])
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

# Функция перевода из скобочной нотации в вектор (принимает список коэффициентов)
def bracket_to_vector_notation(*coefficients):
    return list(coefficients)

# Матрицы, моделирующие, например, квантовые операторы или состояния
A = [[0.707, -0.707], [0.707, 0.707]]  # Матрица поворота на 45 градусов
B = [[0.5, 0.5], [0.5, -0.5]]          # Гейтовая матрица Адамара (Hadamard)
v = [1, 0]                             # Базисное состояние |0⟩
w = [0, 1]                             # Базисное состояние |1⟩
superPos_vector = [0.6, 0.8]           # Состояние суперпозиции

k_A = 2   # Коэффициент для матрицы A
k_B = 1.5 # Коэффициент для матрицы B
k_v = 0.9 # Коэффициент для вектора v
k_w = 1.2 # Коэффициент для вектора w

# Примеры вычислений с коэффициентами
print("=== Примеры вычислений с матрицами и векторами ===\n")

C = matrix_multiplication(A, B, 1, 1)
print_matrix(A, "Матрица A", k_A)
print_matrix(B, "Матрица B", k_B)
print_matrix(C, "Результат умножения A и B с коэффициентами")

Av = matrix_vector_multiplication(A, v, k_A, k_v)
print_matrix(A, "Матрица A", k_A)
print_vector(v, "Вектор v", k_v)
print_vector(Av, "Результат умножения матрицы A на вектор v с коэффициентами")

tensor_AB = tensor_product_matrixes(A, B, k_A, k_B)
print_matrix(tensor_AB, "Тензорное произведение матриц A и B с коэффициентами")

tensor_vw = tensor_product_vectors(v, w, k_v, k_w)
print_vector(v, "Вектор v", k_v)
print_vector(w, "Вектор w", k_w)
print_vector(tensor_vw, "Результат тензорного произведения векторов v и w с коэффициентами")

print("Вектор в скобочной нотации : ", vector_to_bracket_notation(superPos_vector, k_v))

k_tensor_vw = 1
print("Вектор в скобочной нотации : ", vector_to_bracket_notation(tensor_vw, k_tensor_vw))