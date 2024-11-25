import random

# Генерация кубита (состояния) пользователем A
def generate_qubit():
    states = ["|0⟩", "|1⟩", "|0'⟩", "|1'⟩"]
    return random.choice(states)

# Выбор измерительного базиса пользователем B
def choose_basis():
    bases = ["|0⟩, |1⟩", "|0'⟩, |1'⟩"]
    return random.choice(bases)

# Измерение кубита в выбранном базисе
def measure(qubit, basis):
    if correct_basis(qubit, basis):
        # Результат детерминированный
        # print("Результат детерминированный")
        return 0 if qubit in ["|0⟩", "|0'⟩"] else 1
    else:
        # Результат случайный
        # print("Результат случайный")
        return random.choice([0, 1])

# Проверка, сгенерированный кубит измерителю
def correct_basis(qubit, basis):
    return (qubit in ["|0⟩", "|1⟩"] and basis == "|0⟩, |1⟩") or \
            (qubit in ["|0'⟩", "|1'⟩"] and basis == "|0'⟩, |1'⟩")

def quantum_key_distribution():
    secret_key = []
    num_of_bits = int(input("Введите количество битов секретного ключа: "))

    for _ in range(num_of_bits):
        finished = False
        while not finished:
            # A генерирует кубит
            qubit = generate_qubit()
            print(f"A: Сгенерирован кубит {qubit}")

            # B выбирает базис
            basis_b = choose_basis()
            print(f"B: Выбран базис {basis_b}")

            # B измеряет кубит
            measurement_result = measure(qubit, basis_b)
            print(f"B: Результат измерения {measurement_result}")

            # B сообщает A базис
            print(f"B -> A: Использован базис {basis_b}")

            # A проверяет базис и решает, продолжать или нет
            if correct_basis(qubit, basis_b):
                print("A -> B: OK\n")
                # Определение секретного бита
                secret_bit = 0 if qubit in ["|0⟩", "|0'⟩"] else 1
                # print(f"Добавлено: {secret_bit}\n")
                secret_key.append(secret_bit)
                finished = True
            else:
                print(f"A -> B: ПОВТОР\n")

    print("Общий секретный ключ: " + '\033[92m' + f"{''.join(map(str, secret_key))}" + '\033[0m')

quantum_key_distribution()