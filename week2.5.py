import sys
input_data = sys.stdin.read().split()
n = int(input_data[0])
q = int(input_data[1])

# Считываем все возможные мосты (проекты)
edges = []
idx = 2
for _ in range(q):
    u = int(input_data[idx])
    v = int(input_data[idx+1])
    c = int(input_data[idx+2])
    # Сохраняем в виде кортежа (стоимость, город1, город2)
    edges.append((c, u, v))
    idx += 3
    
# Сортируем мосты по возрастанию стоимости (для алгоритма Краскала)
edges.sort()

# Инициализация массивов, точно как в первой задаче:
# parent[x] хранит родителя элемента x
parent = list(range(n + 1))
# size[x] хранит размер множества (для взвешенного объединения)
size = [1] * (n + 1)

# Функция FIND-SET со сжатием пути
def find(i):
    root = i
    # Ищем корень
    while root != parent[root]:
        root = parent[root]
    # Сжатие пути: все узлы на пути теперь указывают прямо на корень
    curr = i
    while curr != root:
        nxt = parent[curr]
        parent[curr] = root
        curr = nxt
    return root

# Функция UNION с объединением по размеру
def union(i, j):
    root_i = find(i)
    root_j = find(j)
    if root_i != root_j:
        # Всегда присоединяем меньшее дерево к большему
        if size[root_i] < size[root_j]:
            root_i, root_j = root_j, root_i
        parent[root_j] = root_i
        # Обновляем размер нового корня
        size[root_i] += size[root_j]
        return True # Объединение прошло успешно (мост нужен)
    return False # Города уже были в одной сети (цикл, мост не нужен)
total_cost = 0
bridges_built = 0
# Алгоритм Краскала
for c, u, v in edges:
    # Пытаемся объединить города u и v
    if union(u, v):
        total_cost += c
        bridges_built += 1     
        # Если мы построили N - 1 мост, значит все города соединены
        if bridges_built == n - 1:
            break         
# Проверяем, удалось ли объединить всё королевство
# Если городов 1, то мостов строить не нужно (n - 1 == 0)
if bridges_built == n - 1 or n == 1:
    print(total_cost)
else:
    # Если мостов меньше чем n - 1, значит граф несвязный
    print(-1)
