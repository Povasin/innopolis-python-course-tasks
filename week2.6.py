# # Коэффиценты хэширования p=31 а q = 1000000007 (огромное число) чтобы уменьшить вероятность коллизии. а коэф p будет брать 31 так как это число простое оно больше кол-во латинский букв в алфавите. и с ним можно легко работь при помощи побитовых сдвигов
# import sys
# line1 = sys.stdin.readline().split()
# n, m = map(int, line1)
# text = sys.stdin.readline()
# patterns = []
# for _ in range(m):
#     patterns.append(sys.stdin.readline().strip())
# d = 31
# q = 10**9 + 7
# l_len = len(patterns[0])
# t_lower = text.lower()
# # Словарь для хранения индексов по хешам: {хеш: [индексы]}
# hash_map = {}
# # Предвычисление d^(L-1) mod q
# h_pow = pow(d, l_len - 1, q)
# # Вычисляем хеш первого окна
# current_hash = 0
# for i in range(l_len):
#     current_hash = (d * current_hash + (ord(t_lower[i]))) % q
# hash_map.setdefault(current_hash, []).append(0)

# # Скользящее окно по тексту
# for s in range(n - l_len):
#     # Удаляем символ слева, добавляем символ справа
#     prev_char = ord(t_lower[s])
#     next_char = ord(t_lower[s + l_len])
    
#     current_hash = (d * (current_hash - prev_char * h_pow) + next_char) % q
    
#     # Индексы в словаре будут автоматически отсортированы по возрастанию
#     if current_hash not in hash_map:
#         hash_map[current_hash] = []
#     hash_map[current_hash].append(s + 1)

# output = []
# for p in patterns:
#     p_lower = p.lower()
#     # Считаем хеш образца
#     p_hash = 0
#     for char in p_lower:
#         p_hash = (d * p_hash + ord(char)) % q
        
#     found_indices = []
#     if p_hash in hash_map:
#         # проверка по символьноая сравниваем образец и хэш 
#         for idx in hash_map[p_hash]:
#             if t_lower[idx : idx + l_len] == p_lower:
#                 found_indices.append(idx)
#     line = [str(len(found_indices))] + list(map(str, found_indices))
#     output.append(" ".join(line))
# sys.stdout.write("\n".join(output) + "\n")


import sys

def build_table(P, M):
    # Создает таблицу переходов для образца P.
    # table[состояние][символ] = новое_состояние (длина префикса).
    table = []
    
    for q in range(M + 1):
        row = {}
        # Пробуем добавить каждую букву латинского алфавита
        for char_code in range(ord('a'), ord('z') + 1):
            c = chr(char_code)
            
            # Строим строку: текущий префикс + новый символ 
            s = P[:q] + c
            
            # Ищем самый длинный префикс P, который является суффиксом s
            # Начинаем с максимально возможной длины и уменьшаем её
            next_q = 0
            for length in range(min(M, len(s)), 0, -1):
                if s.endswith(P[:length]):
                    next_q = length
                    break
            row[c] = next_q
        table.append(row)
    return table

input_data = sys.stdin.read().split()
n = int(input_data[0])
m = int(input_data[1])
k = int(input_data[2])
text = input_data[3]
p1 = input_data[4]
p2 = input_data[5]

# Шаг 1: Предвычисление таблиц переходов (предобработка)
table1 = build_table(p1, m)
table2 = build_table(p2, m)

# Шаг 2: Моделирование работы на тексте
q1, q2 = 0, 0
results = []

for char in text:
    # Обновляем состояния обоих автоматов
    q1 = table1[q1][char]
    q2 = table2[q2][char]
    
    # Нас интересует максимальное совпадение среди всех образцов
    results.append(max(q1, q2))

# Печать результата одной строкой
print(*(results))
