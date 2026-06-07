import sys
from collections import deque

# Алгоритм: Эдмондса-Карпа (на базе BFS)
data = sys.stdin.read().split()
N, M, S, T = map(int, data[:4])

capacity = [[0] * (N + 1) for _ in range(N + 1)]
flow = [[0] * (N + 1) for _ in range(N + 1)]
adj = [[] for _ in range(N + 1)]

for i in range(M):
    u, v, b = int(data[4 + i*3]), int(data[5 + i*3]), int(data[6 + i*3])
    capacity[u][v] = b
    adj[u].append(v)
    adj[v].append(u)

max_flow = 0
first_iteration = True
reachable_at_start = False

# Основной цикл алгоритма Эдмондса-Карпа
while True:
    parent = {S: None}
    queue = deque([S])
    path_found = False
    
    while queue:
        u = queue.popleft()
        if u == T:
            path_found = True
            if first_iteration: reachable_at_start = True
            break
        
        for v in adj[u]:
            if v not in parent and capacity[u][v] - flow[u][v] > 0:
                parent[v] = u
                queue.append(v)
        if path_found:
            break
    
    if first_iteration and not path_found:
        # Если на первой итерации путь не найден, T недостижим
        print("UNREACHABLE")
        exit()
    
    first_iteration = False
    if not path_found:
        break
        
    path_flow = float('inf')
    curr_node = T
    while curr_node != S:
        prev_node = parent[curr_node]
        path_flow = min(path_flow, capacity[prev_node][curr_node] - flow[prev_node][curr_node])
        curr_node = prev_node
    
    max_flow += path_flow
    curr_node = T
    while curr_node != S:
        prev_node = parent[curr_node]
        flow[prev_node][curr_node] += path_flow
        flow[curr_node][prev_node] -= path_flow
        curr_node = prev_node

# После нахождения макс. потока, находим все достижимые вершины из S в G_f
s_set = []
visited = [False] * (N + 1)
visited[S] = True
q = deque([S])

while q:
    u = q.popleft()
    s_set.append(u)
    for v in adj[u]:
        if not visited[v] and capacity[u][v] - flow[u][v] > 0:
            visited[v] = True
            q.append(v)

# Формируем множество T
t_set = [i for i in range(1, N + 1) if not visited[i]]

# Вывод результатов
sys.stdout.write(f"{max_flow}\n")

sys.stdout.write(f"{len(s_set)}\n")
sys.stdout.write(" ".join(map(str, s_set)) + "\n")

sys.stdout.write(f"{len(t_set)}\n")
sys.stdout.write(" ".join(map(str, t_set)) + "\n")
