import numpy as np

# Функция для моделирования измерения отдельного кубита в регистре
def measure_single_qubit(state, qubit_index):
    # Вычисление вероятностей получения 0 или 1 на указанном кубите
    probability_0 = sum(abs(amplitude)**2 for i, amplitude in enumerate(state) if not (i >> qubit_index) & 1)
    probability_1 = sum(abs(amplitude)**2 for i, amplitude in enumerate(state) if (i >> qubit_index) & 1)
    
    # Нормализация вероятностей
    probability_0 = round(probability_0, 2)
    probability_1 = round(probability_1, 2)
    probabilities = [probability_0, probability_1]
    
    # Измерение кубита: выбор результата на основе рассчитанных вероятностей
    result = np.random.choice([0, 1], p=probabilities)
    
    # "Схлопывание" регистра: исключение несовместимых с результатом состояний
    new_state = np.zeros_like(state)
    for i in range(len(state)):
        if ((i >> qubit_index) & 1) == result:
            new_state[i] = state[i] / np.sqrt(probabilities[result]) if probabilities[result] > 0 else 0
    
    # Округление элементов нового состояния до двух знаков
    new_state = np.round(new_state, 4)
    
    return result, new_state, probabilities

# Функция для перевода состояния в скобочную нотацию (бра-кет нотация)
def state_to_bracket_notation(state):
    terms = []
    for i, amplitude in enumerate(state):
        if amplitude != 0:
            terms.append(f"{amplitude:.4f}|{i:02b}⟩")
    return " + ".join(terms)

# Функция перевода вектора в скобочную нотацию
def vector_to_bracket_notation(v, k=1):
    if len(v) == 2:
        return f"{v[0]:.2f}|0⟩ + {v[1]:.2f}|1⟩"
    else:
        n = len(v)
        num_qubits = (n - 1).bit_length()  # Определяем количество кубитов
        notation = " + ".join(f"{k * k_v:.2f}|{format(i, f'0{num_qubits}b')}⟩" for i, k_v in enumerate(v) if k * k_v != 0)
        return notation

# Пример 1: Измерение первого кубита (с индексом 0)
state = np.array([0.5, 0.5, 0.5, 0.5])  # Суперпозиция

result_0, new_state_0, probabilities_0 = measure_single_qubit(state, 0)

print("\nПример 1: Измерение первого кубита (с индексом 0):")
print("Вектор в скобочной нотации:", vector_to_bracket_notation(state))
print(f"Измеренный кубит: {'|1⟩' if result_0 == 1 else '|0⟩'}")
print(f"Вероятности: |0⟩ -> {probabilities_0[0]}, |1⟩ -> {probabilities_0[1]}")
print("Новое состояние квантового регистра после измерения:")
print(state_to_bracket_notation(new_state_0))
print("\n" + "#" * 69 + "\n")

# Пример 2: Измерение второго кубита (с индексом 1)
result_1, new_state_1, probabilities_1 = measure_single_qubit(state, 1)

print("Пример 2: Измерение второго кубита (с индексом 1):")
print("Вектор в скобочной нотации:", vector_to_bracket_notation(state))
print(f"Измеренный кубит: {'|1⟩' if result_1 == 1 else '|0⟩'}")
print(f"Вероятности: |0⟩ -> {probabilities_1[0]}, |1⟩ -> {probabilities_1[1]}")
print("Новое состояние квантового регистра после измерения:")
print(state_to_bracket_notation(new_state_1))
