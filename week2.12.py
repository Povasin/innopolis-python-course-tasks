# import sys
# import heapq
# input_data = sys.stdin.read().splitlines()
# Q = int(input_data[0])

# # Храним граф в виде словаря словарей
# adj = {}
# active_branches = set()

# for i in range(1, Q + 1):
#     line = input_data[i].split()
#     if not line:
#         continue
    
#     operation = line[0]

#     if operation == 'add':
#         x = line[1]
#         active_branches.add(x)
#         adj[x] = {}

#     elif operation == 'remove':
#         x = line[1]
#         # Удаляем ребра, ведущие к x, у всех соседей
#         for neighbor in adj[x]:
#             if x in adj[neighbor]:
#                 del adj[neighbor][x]
#         # Удаляем сам филиал
#         del adj[x]
#         active_branches.remove(x)

#     elif operation == 'connect':
#         u, v, c = line[1], line[2], int(line[3])
#         adj[u][v] = c
#         adj[v][u] = c

#     elif operation == 'disconnect':
#         u, v = line[1], line[2]
#         if v in adj[u]:
#             del adj[u][v]
#         if u in adj[v]:
#             del adj[v][u]

#     elif operation == 'expand':
#         st = line[1]
        
#         # Реализация алгоритма Прима 
#         # (priority, current_node, parent_node)
#         pq = [(0, st, None)]
#         visited = set()
#         total_mst_cost = 0
#         mst_edges = []
        
#         while pq:
#             cost, u, p = heapq.heappop(pq)
            
#             if u in visited:
#                 continue
            
#             visited.add(u)
#             total_mst_cost += cost
            
#             if p is not None:
#                 mst_edges.append((p, u, cost))
            
#             # Просматриваем соседей извлеченной вершины 
#             for v, weight in adj[u].items():
#                 if v not in visited:
#                     # В кучу добавляем вершину с весом ребра к ней
#                     heapq.heappush(pq, (weight, v, u))
    
#         sys.stdout.write(f"{total_mst_cost}\n")
#         for u, v, w in mst_edges:
#             sys.stdout.write(f"{u} {v} {w}\n")


import sys
class DSU:
    def __init__(self, elements):
        # Инициализация: каждая вершина — сама себе родитель, ранг 0
        self.parent = {obj: obj for obj in elements}
        self.rank = {obj: 0 for obj in elements}

    def find(self, i):
        # Поиск с использованием эвристики сжатия путей
        if self.parent[i] == i:
            return i
        self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i, j):
        # Объединение по рангу
        root_i = self.find(i)
        root_j = self.find(j)
        if root_i != root_j:
            if self.rank[root_i] < self.rank[root_j]:
                self.parent[root_i] = root_j
            elif self.rank[root_i] > self.rank[root_j]:
                self.parent[root_j] = root_i
            else:
                self.parent[root_i] = root_j
                self.rank[root_j] += 1
            return True
        return False

input_data = sys.stdin.read().splitlines()
Q = int(input_data[0])

cities = set()
# Храним планы как словарь: (min_v, max_v) -> cost
plans = {}
# Для эффективного удаления города храним список инцидентных ему планов
city_to_neighbors = {}

for i in range(1, Q + 1):
    line = input_data[i].split()
    if not line: continue
    
    op = line[0]
    
    if op == 'add':
        city = line[1]
        cities.add(city)
        city_to_neighbors[city] = set()
        
    elif op == 'remove':
        city = line[1]
        # Удаляем все связанные планы у соседей
        neighbors = list(city_to_neighbors[city])
        for neighbor in neighbors:
            edge = tuple(sorted((city, neighbor)))
            if edge in plans:
                del plans[edge]
            if city in city_to_neighbors[neighbor]:
                city_to_neighbors[neighbor].remove(city)
        # Удаляем сам город
        cities.remove(city)
        del city_to_neighbors[city]
        
    elif op == 'plan':
        u, v, c = line[1], line[2], int(line[3])
        edge = tuple(sorted((u, v)))
        plans[edge] = c
        city_to_neighbors[u].add(v)
        city_to_neighbors[v].add(u)
        
    elif op == 'unplan':
        u, v = line[1], line[2]
        edge = tuple(sorted((u, v)))
        if edge in plans:
            del plans[edge]
            city_to_neighbors[u].remove(v)
            city_to_neighbors[v].remove(u)
            
    elif op == 'construct':
        # 1. Подготовка рёбер и их сортировка
        all_edges = []
        for (u, v), cost in plans.items():
            all_edges.append((cost, u, v))
        
        # Сортировка по весу (основной этап Крускала)
        all_edges.sort()
        
        # 2. Инициализация DSU для всех текущих городов
        dsu = DSU(cities)
        
        mst_cost = 0
        mst_edges = []
        
        # 3. Проход по отсортированным рёбрам
        for cost, u, v in all_edges:
            if dsu.union(u, v):
                mst_cost += cost
                mst_edges.append(f"{u} {v} {cost}")

        sys.stdout.write(f"{mst_cost}\n")
        if mst_edges:
            sys.stdout.write("\n".join(mst_edges) + "\n")