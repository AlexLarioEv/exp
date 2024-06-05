import csv
from params import dataBreath


# print(dataBreath)
# Извлечение заголовков
headers = list(dataBreath.keys())

# Подготовка строк данных
rows = []  # Начнем с заголовков

# Найдем максимальную длину списка значений
max_length = max(len(values) for values in dataBreath.values())

# Создаем строки данных
for i in range(max_length):
    row = []
    for key in headers:
        # Добавляем значение или пустую строку, если значений меньше максимальной длины
        row.append(str(dataBreath[key][i]) if i < len(dataBreath[key]) else "")
    rows.append(row)

print(rows)

# Открытие файла для записи начальных данных 
# with open('./db/statistics/dataBreath.csv', 'w', newline='', encoding='utf-8') as file:
#     writer = csv.writer(file)
#     writer.writerows(rows)

# Открытие файла для добавления данных в конец файла 
with open('./db/statistics/dataBreath.csv', 'a', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerows(rows)