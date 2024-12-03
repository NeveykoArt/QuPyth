import numpy as np

# Функция для моделирования измерения квантового регистра
def measure_quantum_register(state):
    # Вычисление вероятностей для каждого состояния (квадрат модуля амплитуды)
    probabilities = [round(abs(amplitude)**2, 2) for amplitude in state]
    
    # Нормализация вероятностей до 1, если сумма не равна 1
    probabilities = [p / sum(probabilities) for p in probabilities]
    
    # Выполнение измерения с выбором состояния на основе вероятностей
    result = np.random.choice(range(len(state)), p=probabilities)
    return result, probabilities

# Регистр, состоящий из 4 состояний, моделирующий суперпозицию
superPos_state = np.array([0.5, 0.5, 0.5, 0.5])

# Функция перевода вектора в скобочную нотацию
"""def vector_to_bracket_notation(v):
    return f"{v[0]:.2f}|00⟩ + {v[1]:.2f}|01⟩ + {v[2]:.2f}|10⟩ + {v[3]:.2f}|11⟩"
"""
def vector_to_bracket_notation(v, k=1):
    if len(v) == 2:
        return f"{k * v[0]:.2f}|0⟩ + {k * v[1]:.2f}|1⟩"
    else:
        n = len(v)
        num_qubits = (n - 1).bit_length()  # Определяем количество кубитов
        notation = " + ".join(f"{k * k_v:.2f}|{format(i, f'0{num_qubits}b')}⟩" for i, k_v in enumerate(v) if k * k_v != 0)
        return notation
print("Вектор в скобочной нотации:", vector_to_bracket_notation(superPos_state))

# Измерение квантового регистра
result, probabilities = measure_quantum_register(superPos_state)
print("Измерение квантового регистра:")
print(f"Результат: |{result:2b}⟩, Вероятности: {probabilities}")
