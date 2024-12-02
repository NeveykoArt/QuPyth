import os

print("Выберите задачу для запуска:\n")
print("1. Сервисные подпрограммы")
print("2. Измерение кубита")
print("3. Измерение регистра")
print("4. Измерение отдельных кубитов")

task_num = int(input("Номер задания: "))

while (task_num not in range(1, 5)):
    print("Неправильно введён номер задания (CTRL + C для выхода из программы).\n")
    task_num = int(input("Номер задания: "))

os.system(f"python3 task{task_num}.py")