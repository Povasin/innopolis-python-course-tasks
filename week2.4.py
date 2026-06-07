# N = int(input())
# order = map(int, input().split(' '))
# # Класс для Левой кучи (Максимальной) - ручная реализация
# class MaxHeap:
#     def __init__(self):
#         self.data = []
#         self.size = 0  # Обычная переменная

#     def get_max(self):
#         # В корне всегда находится элемент с максимальным ключом
#         if self.size == 0:
#             return -float('inf')
#         return self.data[0]

#     def insert(self, val):
#         # MAX-HEAP-INSERT: Добавляем в конец и поднимаем вверх
#         self.data.append(val)
#         self.size += 1
#         self._sift_up(self.size - 1)

#     def extract(self):
#         # HEAP-EXTRACT-MAX: Меняем корень с последним, удаляем и чиним
#         if self.size == 0:
#             return None
#         max_val = self.data[0]
#         last_val = self.data.pop()
#         self.size -= 1
#         if self.size > 0:
#             self.data[0] = last_val
#             self._sift_down(0) #  MAX-HEAPIFY
#         return max_val

#     def _sift_up(self, idx):
#         # Поднимаем элемент, пока он больше родителя 
#         while idx > 0:
#             parent = (idx - 1) // 2 # Индекс родителя
#             if self.data[idx] > self.data[parent]:
#                 self.data[idx], self.data[parent] = self.data[parent], self.data[idx]
#                 idx = parent
#             else:
#                 break

#     def _sift_down(self, idx):
#         # Опускаем элемент (MAX-HEAPIFY) 
#         while True:
#             left = 2 * idx + 1  # Левый потомок
#             right = 2 * idx + 2 # Правый потомок
#             largest = idx

#             if left < self.size and self.data[left] > self.data[largest]:
#                 largest = left
#             if right < self.size and self.data[right] > self.data[largest]:
#                 largest = right
            
#             if largest != idx:
#                 self.data[idx], self.data[largest] = self.data[largest], self.data[idx]
#                 idx = largest
#             else:
#                 break

# # Класс для Правой кучи (Минимальной) - ручная реализация
# class MinHeap:
#     def __init__(self):
#         self.data = []
#         self.size = 0

#     def get_min(self):
#         if self.size == 0:
#             return float('inf')
#         return self.data[0]

#     def insert(self, val):
#         self.data.append(val)
#         self.size += 1
#         self._sift_up(self.size - 1)

#     def extract(self):
#         if self.size == 0:
#             return None
#         min_val = self.data[0]
#         last_val = self.data.pop()
#         self.size -= 1
#         if self.size > 0:
#             self.data[0] = last_val
#             self._sift_down(0)
#         return min_val

#     def _sift_up(self, idx):
#         while idx > 0:
#             parent = (idx - 1) // 2
#             if self.data[idx] < self.data[parent]: # МЕНЬШЕ родителя
#                 self.data[idx], self.data[parent] = self.data[parent], self.data[idx]
#                 idx = parent
#             else:
#                 break

#     def _sift_down(self, idx):
#         while True:
#             left = 2 * idx + 1
#             right = 2 * idx + 2
#             smallest = idx

#             if left < self.size and self.data[left] < self.data[smallest]: # Ищем МЕНЬШЕГО
#                 smallest = left
#             if right < self.size and self.data[right] < self.data[smallest]:
#                 smallest = right
            
#             if smallest != idx:
#                 self.data[idx], self.data[smallest] = self.data[smallest], self.data[idx]
#                 idx = smallest
#             else:
#                 break
# max_heap_left = MaxHeap() 
# min_heap_right = MinHeap()

# for item_order in order:
#     if max_heap_left.size == 0 or item_order < max_heap_left.get_max():
#         max_heap_left.insert(item_order)
#     else:
#         min_heap_right.insert(item_order)
#     # балансировка - Если слева элементов больше чем (справа + 1), перекидываем вправо
#     if max_heap_left.size > min_heap_right.size + 1:
#         move_item = max_heap_left.extract()
#         min_heap_right.insert(move_item)
#     elif min_heap_right.size > max_heap_left.size:
#         move_item = min_heap_right.extract()
#         max_heap_left.insert(move_item)
#     total = max_heap_left.size + min_heap_right.size
#     if total % 2 != 0:
#         print(max_heap_left.get_max())
#     else:
#         # Для четного кол-ва берем среднее значение вершин двух куч
#         val = (max_heap_left.get_max() + min_heap_right.get_min()) // 2
#         print(val)


# 1. Сначала объявляем класс
class MinHeap:
    def __init__(self):
        self.data = []
        self.size = 0

    def insert(self, val):
        self.data.append(val)
        self.size += 1
        self._sift_up(self.size - 1)

    def extract(self):
        if self.size == 0:
            return None
        min_val = self.data[0]
        last_val = self.data.pop()
        self.size -= 1
        if self.size > 0:
            self.data[0] = last_val
            self._sift_down(0)
        return min_val

    def _sift_up(self, idx):
        while idx > 0:
            parent = (idx - 1) // 2
            # Сравниваем кортежи (priority, name)
            if self.data[idx] < self.data[parent]: 
                self.data[idx], self.data[parent] = self.data[parent], self.data[idx]
                idx = parent
            else:
                break

    def _sift_down(self, idx):
        while True:
            left = 2 * idx + 1
            right = 2 * idx + 2
            smallest = idx

            if left < self.size and self.data[left] < self.data[smallest]:
                smallest = left
            if right < self.size and self.data[right] < self.data[smallest]:
                smallest = right
            
            if smallest != idx:
                self.data[idx], self.data[smallest] = self.data[smallest], self.data[idx]
                idx = smallest
            else:
                break

N = int(input())
groups = {} 
output = []
for _ in range(N):
    parts = input().split()
    cmd = parts[0]
    if cmd == "create":
        group_id = int(parts[1])
        groups[group_id] = MinHeap()

    elif cmd == "add":
        s = parts[1]           
        x = int(parts[2])      
        y = int(parts[3])      
        groups[y].insert((x, s))

    elif cmd == "execute":
        group_id = int(parts[1])
        if group_id in groups:
            res = groups[group_id].extract()
            if res:
                priority, name = res
                output.append(f"{name} {priority}")

    elif cmd == "merge":
        x = int(parts[1])
        y = int(parts[2])
        z = int(parts[3])
        # Извлекаем кучи. Используем .get() или pop() аккуратно
        # (по условию задачи x и y гарантированно существуют)
        heap_a = groups.pop(x)
        heap_b = groups.pop(y)

        # Эвристика Small-to-Large
        if heap_a.size < heap_b.size:
            target_heap = heap_b
            source_heap = heap_a
        else:
            target_heap = heap_a
            source_heap = heap_b
        
        # Переносим элементы
        for item in source_heap.data:
            target_heap.insert(item)
            
        groups[z] = target_heap
print('\n'.join(output))
