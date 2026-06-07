# import sys

# def compute_prefix_function(P):
#     """Вычисление префикс-функции образца P """
#     m = len(P)
#     pi = [0] * m
#     k = 0
#     for q in range(1, m):
#         while k > 0 and P[k] != P[q]:
#             k = pi[k-1]
#         if P[k] == P[q]:
#             k += 1
#         pi[q] = k
#     return pi

# def kmp_count(T, P):
#     """Поиск количества вхождений образца P в текст T """
#     n = len(T)
#     m = len(P)
#     if m == 0: return 0
#     pi = compute_prefix_function(P)
#     q = 0  # Количество совпавших символов
#     count = 0
#     for i in range(n):
#         while q > 0 and P[q] != T[i]:
#             q = pi[q-1]
#         if P[q] == T[i]:
#             q += 1
#         if q == m:
#             count += 1
#             q = pi[q-1]  # Ищем следующее вхождение (с учетом перекрытий)
#     return count

# # Быстрое чтение входных данных
# lines = sys.stdin.read().splitlines()
# first_line = lines[0].split()
# n = int(first_line[0])
# m = int(first_line[1])

# text = lines[1].lower()
# thresholds = list(map(int, lines[2].split()))
# counts = []
# is_cheater = True

# for i in range(m):
#     pattern = lines[3 + i].lower()
#     c = kmp_count(text, pattern)
#     counts.append(c)
#     if c < thresholds[i]:
#         is_cheater = False
        
# if is_cheater:
#     print("cheater")
# else:
#     print("innocent")
# print(*(counts))

import sys
# Быстрое чтение входных данных
input_data = sys.stdin.read().split()
n = int(input_data[0])
s = input_data[1]
# Начальные ранги на основе ASCII кодов символов
rank = [ord(c) for c in s]

# Сжатие рангов в диапазон [0, n-1]
distinct_ranks = sorted(set(rank))
rank_map = {val: i for i, val in enumerate(distinct_ranks)}
rank = [rank_map[x] for x in rank]

k = 1
while k < n:
    # Формируем пары рангов для подстрок длины 2*k
    # Используем циклическое смещение (i + k) % n
    shifted_rank = rank[k:] + rank[:k]
    
    # Битовая упаковка пары в одно число для ускорения сортировки в Python
    # rank[i] - старшие биты, shifted_rank[i] - младшие
    combined = [(r << 20) | sr for r, sr in zip(rank, shifted_rank)]
    
    # Сортируем индексы на основе комбинированных рангов 
    idx = sorted(range(n), key=combined.__getitem__)
    # Обновляем ранги на основе отсортированного порядка 
    new_rank = [0] * n
    r = 0
    for i in range(1, n):
        if combined[idx[i]] != combined[idx[i-1]]:
            r += 1
        new_rank[idx[i]] = r
    
    rank = new_rank
    # Оптимизация: если все ранги уникальны, дальнейшая сортировка не нужна
    if r == n - 1:
        break
    k *= 2

# Ищем минимальное число правых сдвигов K
# Лексикографически наименьший сдвиг имеет ранг 0
min_k = n
for i in range(n):
    if rank[i] == 0:
        # Если начало сдвига в индексе i, то число правых сдвигов:
        # K = (n - i) % n
        curr_k = (n - i) % n
        if curr_k < min_k:
            min_k = curr_k

print(min_k)