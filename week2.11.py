import sys
from collections import deque
massadj = {}
rev_adj = {} # Вспомогательный словарь, чтобы быстро удалять модули

def COMPILE():
    visited = set()    # Посещенные модули (черные)
    on_stack = set()   # Модули в текущем пути рекурсии (серые - для поиска цикла)
    order = []         # Итоговый порядок
    path_list = []     # Список для восстановления цикла

    def dfs(u):
        visited.add(u)
        on_stack.add(u)
        path_list.append(u)
        
        # Перебор зависимостей: от каких модулей зависит u
        for v in massadj[u]:
            if v in on_stack:
                # Обнаружен цикл. Находим, где он начался в path_list
                idx = path_list.index(v)
                return False, path_list[idx:] + [v]
            
            if v not in visited:
                success, res = dfs(v)
                if not success:
                    return False, res
        
        on_stack.remove(u)
        path_list.pop()
        order.append(u) # Добавляем в конец, когда все зависимости уже обработаны
        return True, None

    # Запускаем DFS от всех модулей
    for m in massadj:
        if m not in visited:
            success, res = dfs(m)
            if not success:
                print("NO")
                print(" ".join(res))
                return

    print("YES")
    print(" ".join(order))

# Считываем Q
line = sys.stdin.readline()
if line:
    Q = int(line.strip())
    for _ in range(Q):
        data = sys.stdin.readline().split()
        cmd = data[0]
        if 'Add' == cmd:
            name = data[1]
            massadj[name] = set()
            rev_adj[name] = set()
            
        elif 'Remove' == cmd:
            name = data[1]
            if name in massadj:
                # Удаляем все связи, где этот модуль был зависимостью
                for dependent in rev_adj[name]:
                    massadj[dependent].discard(name)
                # Удаляем все связи, от которых зависел этот модуль
                for dependency in massadj[name]:
                    rev_adj[dependency].discard(name)
                del massadj[name]
                del rev_adj[name]
                
        elif 'Depend' == cmd:
            name1, name2 = data[1], data[2]
            massadj[name1].add(name2)
            rev_adj[name2].add(name1)
        elif 'Break' == cmd:
            name1, name2 = data[1], data[2]
            massadj[name1].discard(name2)
            rev_adj[name2].discard(name1)
            
        elif 'Compile' == cmd:
            COMPILE()