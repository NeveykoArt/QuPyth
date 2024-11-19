import numpy as np

# Задание 1: Сервисные подпрограммы
def multiplication(a, b):
    res = np.dot(a, b)
    return res

def matrix_tensor_multiplication(a, b):
    res = np.tensordot(a, b, axes=0)
    return res

def vector_in_bra(vector):
    return "<" + ", ".join(map(str, vector)) + "|"

def vector_in_ket(vector):
    return "|" + ", ".join(map(str, vector.flatten())) + ">"

# Задание 2: Измерение кубита
def hadamard_transform(qubit):
    k = 1 / np.sqrt(2)
    H = np.array([[1, 1], [1, -1]])
    return k * np.dot(H, qubit)

def measure_qubit(qubit):
    probabilities = np.abs(qubit) ** 2
    outcome = np.random.choice([0, 1], p=probabilities)
    new_state = np.zeros_like(qubit)
    new_state[outcome] = 1
    return outcome, new_state

# Задание 3: Измерение регистра
def measure_register(register):
    """Измеряет весь регистр."""
    probabilities = np.abs(register) ** 2
    outcome = np.random.choice(len(register), p=probabilities)
    new_state = np.zeros_like(register)
    new_state[outcome] = 1
    return outcome, new_state

# Задание 4: Измерение отдельных кубитов
def measure_single_qubit(register, qubit_index, num_qubits):
    """Измеряет отдельный кубит в регистре."""
    probabilities = []
    for state in range(len(register)):
        bit = (state >> qubit_index) & 1
        probabilities.append(np.abs(register[state]) ** 2 if bit == 1 else 0)

    probabilities = np.array(probabilities, dtype=float)

    total_prob = np.sum(probabilities)
    if np.isclose(total_prob, 0):
        raise ValueError("Сумма вероятностей равна нулю. Убедитесь, что состояние регистра корректно.")
    probabilities /= total_prob  # Нормировка

    # Генерируем результат измерения
    outcome = np.random.choice([0, 1], p=[1 - np.sum(probabilities), np.sum(probabilities)])

    # Формируем новое состояние регистра
    new_register = np.zeros_like(register, dtype=float)
    for state in range(len(register)):
        bit = (state >> qubit_index) & 1
        if bit == outcome:
            new_register[state] = register[state]

    # Нормализация нового регистра
    norm = np.sqrt(np.sum(np.abs(new_register) ** 2))
    if not np.isclose(norm, 0):
        new_register /= norm

    return outcome, new_register

if __name__ == "__main__":
    print('\033[93m' + "ВАЖНАЯ ИНФОРМАЦИЯ:\n" + '\033[0m' + "Чтобы ввести " + '\033[92m' + "1/√2" + '\033[0m' + ", нужно ввести значение: " + '\033[92m' + "0.707106781" + '\033[0m')
    print("Чтобы ввести " + '\033[92m' + "√3/2" + '\033[0m' + ", нужно ввести значение: " + '\033[92m' + "0.866025404\n" + '\033[0m')

    print("Выберите задачу: ")
    print("1. Базовые операции с матрицами и векторами")
    print("2. Моделирование измерения кубита")
    print("3. Моделирование измерения регистра")
    print("4. Моделирование измерения отдельных кубитов")
    choice = int(input("Введите номер задачи: "))

    if choice == 1:
        N = int(input("\nВведите N (степень 2-ки): "))
        print("Введите элементы матрицы 1 через пробел: ")
        entries = list(map(int, input().split()))
        matrix_1 = np.array(entries).reshape(N, N)

        print("Введите элементы матрицы 2 через пробел: ")
        entries = list(map(int, input().split()))
        matrix_2 = np.array(entries).reshape(N, N)

        print("Введите элементы вектора 1 через пробел: ")
        entries = list(map(int, input().split()))
        vector_1 = np.array(entries).reshape(N)

        print("Введите элементы вектора 2 через пробел: ")
        entries = list(map(int, input().split()))
        vector_2 = np.array(entries).reshape(N)

        print("\nУмножение матриц: ")
        print(multiplication(matrix_1, matrix_2))

        print("\nУмножение матрицы на вектор: ")
        print(multiplication(matrix_1, vector_1))

        print("\nТензорное умножение матриц: ")
        print(matrix_tensor_multiplication(matrix_1, matrix_2))

        print("\nТензорное умножение векторов: ")
        print(matrix_tensor_multiplication(vector_1, vector_2))

    elif choice == 2:
        a0 = float(input("\nВведите коэффициент a0: "))
        a1 = float(input("Введите коэффициент a1: "))

        # Проверка на (приближённое) равенство a0^2 + a1^2 == 1
        if not np.isclose(a0**2 + a1**2, 1.0):
            print('\033[91m' + "ОШИБКА:" + '\033[0m' + " a0^2 + a1^2 должно быть равно 1.")
            exit()
        
        qubit = np.array([a0, a1])
        print("Исходное состояние кубита в стандартном базисе:", vector_in_ket(qubit))

        outcome, new_state = measure_qubit(qubit)
        print(f"Измерение в стандартном базисе: результат={outcome}, новое состояние={vector_in_ket(new_state)}")

        rotated_qubit = hadamard_transform(qubit)
        print("Состояние кубита в повернутом базисе:", vector_in_ket(rotated_qubit))

        outcome, new_state = measure_qubit(rotated_qubit)
        print(f"Измерение в повернутом базисе: результат={outcome}, новое состояние={vector_in_ket(new_state)}")

    elif choice == 3:
        n = int(input("\nВведите количество состояний в регистре (должно быть степенью 2): "))
        if n % 2 != 0:
            print('\033[91m' + "ОШИБКА:" + '\033[0m' + " количество состояний в регистре должно быть степенью 2.")
            exit()

        coefficients = list(map(float, input("Введите коэффициенты состояния регистра (нормированы и ввод через пробел): ").split()))
        if len(coefficients) != n:
            print('\033[91m' + "ОШИБКА:" + '\033[0m' + " колличество введенных коэффициентов состояния регистра не совпадает с \'n\'")
            exit()

        register = np.array(coefficients)
        print("Исходное состояние регистра:", vector_in_ket(register))

        outcome, new_state = measure_register(register)
        print(f"Измерение регистра: результат = {outcome}, новое состояние = {vector_in_ket(new_state)}")

    elif choice == 4:
        num_qubits = int(input("\nВведите количество кубитов в регистре: "))
        coefficients = list(map(float, input("Введите коэффициенты состояния регистра (нормированы и ввод через пробел): ").split()))
        register = np.array(coefficients)

        qubit_index = int(input("Введите индекс измеряемого кубита (0-indexed): "))
        outcome, new_register = measure_single_qubit(register, qubit_index, num_qubits)
        print(f"Измерение кубита {qubit_index}: результат = {outcome}, новое состояние = {vector_in_ket(new_register)}")