import numpy as np

# Определим преобразование Адамара
H = np.array([[1 / np.sqrt(2), 1 / np.sqrt(2)], 
              [1 / np.sqrt(2), -1 / np.sqrt(2)]])

# Функция для измерения кубита в стандартном базисе
def measure_in_standard_basis(state):
    probabilities = [round(abs(state[0])**2, 2), round(abs(state[1])**2, 2)]
    result = np.random.choice([0, 1], p=probabilities)
    return result, probabilities

# Функция для измерения кубита в повернутом базисе (с использованием преобразования Адамара)
def measure_in_rotated_basis(state):
    rotated_state = np.dot(H, state)  # Преобразование в повернутый базис
    probabilities = [round(abs(rotated_state[0])**2, 2), round(abs(rotated_state[1])**2, 2)]
    result = np.random.choice([0, 1], p=probabilities)
    return result, probabilities

# Функция перевода вектора в скобочную нотацию
def vector_to_bracket_notation(v, k=1):
    if len(v) == 2:
        return f"{k * v[0]:.2f}|0⟩ + {k * v[1]:.2f}|1⟩"
    else:
        n = len(v)
        num_qubits = (n - 1).bit_length()  # Определяем количество кубитов
        notation = " + ".join(f"{k * k_v:.2f}|{format(i, f'0{num_qubits}b')}⟩" for i, k_v in enumerate(v) if k * k_v != 0)
        return notation

# Состояние кубита 0|0⟩ + 1|1⟩
state = np.array([0, 1])

print("Вектор в скобочной нотации:", vector_to_bracket_notation(state))

# Измерение в стандартном базисе
result_standard, probabilities_standard = measure_in_standard_basis(state)
print("Измерение в стандартном базисе:")
print(f"Результат: |{result_standard}⟩, Вероятности: {probabilities_standard}")

# Измерение в повернутом базисе
result_rotated, probabilities_rotated = measure_in_rotated_basis(state)
print("\nИзмерение в повернутом базисе:")
print(f"Результат: |{result_rotated}⟩, Вероятности: {probabilities_rotated}")
