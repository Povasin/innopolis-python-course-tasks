import sys
sys.setrecursionlimit(10000)

def unit_propagation(clauses, assignment):
    queue = []

    for c in clauses:
        if len(c) == 1:
            queue.append(c[0])

    while queue:
        lit = queue.pop()
        var = abs(lit)
        val = lit > 0

        if var in assignment:
            if assignment[var] != val:
                return None
            continue

        assignment[var] = val

        new_clauses = []
        for c in clauses:
            if lit in c:
                continue
            if -lit in c:
                new_c = [x for x in c if x != -lit]
                if len(new_c) == 0:
                    return None
                if len(new_c) == 1:
                    queue.append(new_c[0])
                new_clauses.append(new_c)
            else:
                new_clauses.append(c)

        clauses = new_clauses

    return clauses


def choose_variable(clauses, assignment):
    for c in clauses:
        for lit in c:
            var = abs(lit)
            if var not in assignment:
                return var
    return None


def dpll(clauses, assignment):
    clauses = unit_propagation(clauses, assignment)
    if clauses is None:
        return None

    if not clauses:
        return assignment

    var = choose_variable(clauses, assignment)
    if var is None:
        return assignment

    for val in [True, False]:
        new_assignment = assignment.copy()
        new_assignment[var] = val

        lit = var if val else -var

        new_clauses = []
        for c in clauses:
            if lit in c:
                continue
            if -lit in c:
                new_c = [x for x in c if x != -lit]
                if len(new_c) == 0:
                    break
                new_clauses.append(new_c)
            else:
                new_clauses.append(c)
        else:
            result = dpll(new_clauses, new_assignment)
            if result is not None:
                return result

    return None


def main():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    clauses = [list(map(int, input().split())) for _ in range(m)]

    result = dpll(clauses, {})

    if result is None:
        print("UNSAT")
    else:
        print("SAT")
        print(" ".join('1' if result.get(i, False) else '0' for i in range(1, n+1)))


if __name__ == "__main__":
    main()
import sys

# Повышаем лимит рекурсии для глубокого дерева DPLL
sys.setrecursionlimit(2000)

class SAT_Solver:
    def __init__(self, num_vars, clauses):
        self.num_vars = num_vars
        self.clauses = clauses
        self.assignment = [0] * (num_vars + 1)  # 0: undef, 1: True, -1: False

    def unit_propagate(self):
        """Реализация продвижения единичных литералов из Лекции 9."""
        changed = True
        while changed:
            changed = False
            for clause in self.clauses:
                unassigned = []
                satisfied = False
                for lit in clause:
                    var = abs(lit)
                    val = 1 if lit > 0 else -1
                    if self.assignment[var] == val:
                        satisfied = True
                        break
                    if self.assignment[var] == 0:
                        unassigned.append(lit)
                
                if satisfied:
                    continue
                if not unassigned:
                    return False  # Конфликт
                if len(unassigned) == 1:
                    lit = unassigned[0]
                    self.assignment[abs(lit)] = 1 if lit > 0 else -1
                    changed = True
        return True

    def solve(self):
        """Классический алгоритм DPLL с возвратами."""
        if not self.unit_propagate():
            return False

        # Выбираем следующую неназначенную переменную
        var = 0
        for i in range(1, self.num_vars + 1):
            if self.assignment[i] == 0:
                var = i
                break
        x
        if var == 0:
            return True  # Решение найдено

        state = list(self.assignment)

        # Пробуем True
        self.assignment[var] = 1
        if self.solve():
            return True
        
        # Откат и проба False
        self.assignment = state
        self.assignment[var] = -1
        if self.solve():
            return True
            
        return False

# Чтение входных данных
line1 = sys.stdin.readline().split()
n, l_bag, w_bag = map(int, line1)
lengths = list(map(int, sys.stdin.readline().split()))

# 1. Генерация возможных позиций (i, row, col)
placements = []
box_vars = [[] for _ in range(n)]

for i in range(n):
    box_len = lengths[i]
    for r in range(1, w_bag + 1):
        for c in range(1, l_bag - box_len + 2):
            var_idx = len(placements) + 1
            placements.append({'id': i, 'r': r, 'c': c, 'len': box_len})
            box_vars[i].append(var_idx)

clauses = []

# 2. Формирование ограничений КНФ
# Каждая пачка должна быть хотя бы в одном месте
for i in range(n):
    if not box_vars[i]:
        print("UNSAT")
    clauses.append(box_vars[i])

# Пачка не может быть в двух местах одновременно
for i in range(n):
    vars_i = box_vars[i]
    for idx_a in range(len(vars_i)):
        for idx_b in range(idx_a + 1, len(vars_i)):
            clauses.append([-vars_i[idx_a], -vars_i[idx_b]])

# Проверка перекрытий пачек в багажнике
for a in range(len(placements)):
    for b in range(a + 1, len(placements)):
        p1, p2 = placements[a], placements[b]
        if p1['id'] == p2['id']: continue
        
        if p1['r'] == p2['r']:
            # Проверка пересечения отрезков в одном ряду
            if max(p1['c'], p2['c']) < min(p1['c'] + p1['len'], p2['c'] + p2['len']):
                clauses.append([-(a + 1), -(b + 1)])

# 3. Запуск решателя
solver = SAT_Solver(len(placements), clauses)
if solver.solve():
    print("SAT")
    results = [None] * n
    for i, val in enumerate(solver.assignment[1:]):
        if val == 1:
            p = placements[i]
            results[p['id']] = (p['r'], p['c'])
    
    for res in results:
        print(f"{res[0]} {res[1]}")
else:
    print("UNSAT")
