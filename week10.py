# # # # k.povasin@innopolis.university
# # # # Идея решения была взята из лекции неделя 10 слайд 7ы
# # #  вдохновлялся https://translated.turbopages.org/proxy_u/en-ru.ru.94fd084b-69203911-0661f122-74722d776562/https/www.w3schools.com/PYTHON/python_dsa_avltrees.asp
# # class Node:
# #     def __init__(self, key, value):
# #         self.key = key # ключ узла
# #         self.value = value # содержимое узла
# #         self.height = 1 # на какой высоте узел
# #         self.left = None # левый потомок
# #         self.right = None # правый потомок

# # class AVLTree:
# #     def __init__(self):
# #         self.current = None # текущий узел
# #         self.rotation_count = 0  # счетчик поворотов
# #     def height(self, node): # высота узла
# #         if not node:
# #             return 0
# #         return node.height  
# #     def balance_factor(self, node): # проверка баланса дерева
# #         if not node:
# #             return 0
# #         return self.height(node.left) - self.height(node.right) # если разница больше модуля 1  значит нужно делать повороты
# #     def left_rotate(self, usel): # левый поворот
# #         self.rotation_count += 1
# #         y = usel.right # беру правый узел
# #         T2 = y.left # беру левый узел у этого исходного узла (потомка)
# #         y.left = usel # меняю местами
# #         usel.right = T2
# #         usel.height = 1 + max(self.height(usel.left), self.height(usel.right))
# #         y.height = 1 + max(self.height(y.left), self.height(y.right))
# #         return y
# #     def right_rotate(self, usel): # правый поворот теже действия что и с левым повротом
# #         self.rotation_count += 1
# #         y = usel.left
# #         T3 = y.right
# #         y.right = usel
# #         usel.left = T3
# #         usel.height = 1 + max(self.height(usel.left), self.height(usel.right))
# #         y.height = 1 + max(self.height(y.left), self.height(y.right))
# #         return y

# #     def insert(self, node, key, value): # вставка
# #         if not node:
# #             return Node(key, value)
# #         if key < node.key:
# #             # рекурсивно спускаюсь по дереву влево
# #             node.left = self.insert(node.left, key, value)
# #         elif key > node.key:
# #             # рекурсивно спускаюсь по дереву вправо
# #             node.right = self.insert(node.right, key, value)
# #         else:
# #             # Ключ уже существует
# #             return node
# #         # получаю высоту дерева
# #         node.height = 1 + max(self.height(node.left), self.height(node.right))
# #         # проверяю баланс
# #         balance = self.balance_factor(node)
# #         # левый поворот так как дерево ломается слева
# #         if balance > 1 and key < node.left.key:
# #             return self.right_rotate(node)
# #         # правый поворот так как дерево ломается справа
# #         if balance < -1 and key > node.right.key:
# #             return self.left_rotate(node)
# #         # левый-правый поворот так как дерево ломается сначала слева потом справа из-за значение ключа
# #         if balance > 1 and key > node.left.key:
# #             node.left = self.left_rotate(node.left)
# #             return self.right_rotate(node)
# #         # правый-левый поворот так как дерево ломается сначала справа потом слева из-за значение ключа
# #         if balance < -1 and key < node.right.key:
# #             node.right = self.right_rotate(node.right)
# #             return self.left_rotate(node)
# #         return node

# #     def min_value_node(self, node):
# #         current = node
# #         while current.left:
# #             current = current.left
# #         return current

# #     def delete(self, node, key): # удаление
# #         if not node:
# #             return node

# #         if key < node.key:
# #             node.left = self.delete(node.left, key)
# #         elif key > node.key:
# #             node.right = self.delete(node.right, key)
# #         else:
# #             if not node.left:
# #                 return node.right
# #             elif not node.right:
# #                 return node.left
# #             else:
# #                 temp = self.min_value_node(node.right)
# #                 node.key = temp.key
# #                 node.value = temp.value
# #                 node.right = self.delete(node.right, temp.key)

# #         if not node:
# #             return node

# #         node.height = 1 + max(self.height(node.left), self.height(node.right))
# #         balance = self.balance_factor(node)

# #         # левый поворот 
# #         if balance > 1 and self.balance_factor(node.left) >= 0:
# #             return self.right_rotate(node)

# #         # лево-правый поворот
# #         if balance > 1 and self.balance_factor(node.left) < 0:
# #             node.left = self.left_rotate(node.left)
# #             return self.right_rotate(node)

# #         # правый поворот 
# #         if balance < -1 and self.balance_factor(node.right) <= 0:
# #             return self.left_rotate(node)

# #         # право - левый поворот
# #         if balance < -1 and self.balance_factor(node.right) > 0:
# #             node.right = self.right_rotate(node.right)
# #             return self.left_rotate(node)

# #         return node

# #     def search(self, node, key): # поиск ключа
# #         if not node:
# #             return None
# #         if node.key == key:
# #             return node
# #         elif key < node.key:
# #             return self.search(node.left, key)  # рекурсивно спускаюсь по дереву
# #         else:
# #             return self.search(node.right, key)

# #     def add(self, key, value):
# #         # Проверяем, существует ли ключ
# #         if self.search(self.current, key):
# #             return "KEY ALREADY EXISTS"
# #         self.current = self.insert(self.current, key, value) # добавление ключа
# #         return None

# #     def lookup(self, key):  
# #         node = self.search(self.current, key) # вывод значения узла
# #         if node:
# #             return node.value
# #         return "KEY NOT FOUND"

# #     def delete_key(self, key):
# #         if not self.search(self.current, key):
# #             return "KEY NOT FOUND"
# #         self.current = self.delete(self.current, key)
# #         return None
# #     def print_rotations(self):
# #         return self.rotation_count
# # import sys
# # input = sys.stdin.read
# # data = input().splitlines()
# # n = int(data[0])
# # tree = AVLTree()
# # results = []
# # for i in range(1, n + 1):
# #     command = data[i].split()
# #     cmd_type = command[0]
# #     if cmd_type == "ADD":
# #         result = tree.add(int(command[1]), int(command[2]))
# #         if result:
# #             results.append(result)
# #     elif cmd_type == "LOOKUP":
# #         result = tree.lookup(int(command[1]))
# #         results.append(str(result))
# #     elif cmd_type == "DELETE":
# #         result = tree.delete_key(int(command[1]))
# #         if result:
# #             results.append(result)    
# #     elif cmd_type == "PRINT_ROTATIONS":
# #         result = tree.print_rotations()
# #         results.append(str(result))
# # for i in results:
# #     print(i)



# # k.povasin@innopolis.university
# # вдохновлялся https://habr.com/ru/articles/799137/
# class Node:
#     def __init__(self, key, value):
#         self.key = key  # ключ узла
#         self.value = value  # содержимое узла
#         self.color = "RED"  # цвет узла (новые узлы всегда красные)
#         self.left = None  # левый потомок
#         self.right = None  # правый потомок
#         self.parent = None  # родительский узел

# class RedBlackTree:
#     def __init__(self):
#         self.list = Node(None, None)  # лист узел
#         self.list.color = "BLACK"
#         self.root = self.list  # корень дерева
#         self.rotation_count = 0  # счетчик поворотов
#         self.red_count = 0  # счетчик красных узлов
#         self.black_count = 0  # счетчик черных узлов
    
#     def is_red(self, node):
#         # проверка красный узел
#         return node != self.list and node.color == "RED"
    
#     def is_black(self, node):
#        # проверка черный узел
#         return node == self.list or node.color == "BLACK"
    
#     def left_rotate(self, x):
#         # левый поворот
#         self.rotation_count += 1
#         y = x.right  # устанавливаем y
#         x.right = y.left  # превращаем левое поддерево y в правое поддерево x
#         if y.left != self.list:
#             y.left.parent = x
#         y.parent = x.parent  # переносим родителя x к y
#         if x.parent == self.list:
#             self.root = y
#         elif x == x.parent.left:
#             x.parent.left = y
#         else:
#             x.parent.right = y
#         y.left = x  # помещаем x слева от y
#         x.parent = y
#     def right_rotate(self, x):
#         # правый поворот
#         self.rotation_count += 1
#         y = x.left  # устанавливаем y
#         x.left = y.right  # превращаем правое поддерево y в левое поддерево x
#         if y.right != self.list:
#             y.right.parent = x
#         y.parent = x.parent  # переносим родителя x к y
#         if x.parent == self.list:
#             self.root = y
#         elif x == x.parent.right:
#             x.parent.right = y
#         else:
#             x.parent.left = y
#         y.right = x  # помещаем x справа от y
#         x.parent = y
#     def balance(self, check):
#         # Востонавление баланса дерева
#         while self.is_red(check.parent):
#             if check.parent == check.parent.parent.left: 
#                 y = check.parent.parent.right # родителей
#                 if self.is_red(y): # родителей красный
#                     # Случай 1: родитель красный - перекрашиваем
#                     check.parent.color = "BLACK"
#                     y.color = "BLACK"
#                     check.parent.parent.color = "RED"
#                     check = check.parent.parent
#                 else:
#                     if check == check.parent.right:
#                         # Случай 2: check - правый ребенок - делаем левый поворот
#                         check = check.parent
#                         self.left_rotate(check)
                    
#                     # Случай 3: check - левый ребенок - делаем правый поворот и перекрашиваем
#                     check.parent.color = "BLACK"
#                     check.parent.parent.color = "RED"
#                     self.right_rotate(check.parent.parent)
#             else:
#                 # Симметричный случай, когда родитель является правым ребенком
#                 y = check.parent.parent.left  # дядя check
#                 if self.is_red(y):
#                     # Случай 1: дядя красный - перекрашиваем
#                     check.parent.color = "BLACK"
#                     y.color = "BLACK"
#                     check.parent.parent.color = "RED"
#                     check = check.parent.parent
#                 else:
#                     if check == check.parent.left:
#                         # Случай 2: check - левый ребенок - делаем правый поворот
#                         check = check.parent
#                         self.right_rotate(check)
                    
#                     # Случай 3: check - правый ребенок - делаем левый поворот и перекрашиваем
#                     check.parent.color = "BLACK"
#                     check.parent.parent.color = "RED"
#                     self.left_rotate(check.parent.parent)
        
#         # Корень всегда должен быть черным
#         self.root.color = "BLACK"
    
#     def insert(self, key, value):
#         # Создаем новый узел
#         check = Node(key, value)
#         check.left = self.list
#         check.right = self.list
#         check.parent = self.list
#         # Ищем место для вставки (обычная вставка в бинарное дерево поиска)
#         y = self.list
#         x = self.root
#         while x != self.list:
#             y = x
#             if check.key < x.key:
#                 x = x.left
#             elif check.key > x.key:
#                 x = x.right
#             else:
#                 # Ключ уже существует
#                 return "KEY ALREADY EXISTS"
#         # Устанавливаем родителя для нового узла
#         check.parent = y
#         if y == self.list:
#             self.root = check  # дерево было пустым
#         elif check.key < y.key:
#             y.left = check
#         else:
#             y.right = check
#         # Восстанавливаем свойства красно-черного дерева
#         self.balance(check)
#         return None
    
#     def transplant(self, u, v):
#         # доп функция для удаления при удалении узла с двумя деться нам нужно найти приемника для замены удаленног узла и мы должны брать праый узел по правилу авл дерева
#         if u.parent == self.list:
#             self.root = v
#         elif u == u.parent.left:
#             u.parent.left = v
#         else:
#             u.parent.right = v
#         v.parent = u.parent
    
#     def delete_fixup(self, x):
#         # востонавнилваем баланс после удаления  когда удаляем черный узел так как при удалении красного узла баланс не нарушается
#         while x != self.root and self.is_black(x):
#             if x == x.parent.left:
#                 w = x.parent.right  # ребенок x
                
#                 if self.is_red(w): 
#                     # Случай 1: ребенок красный
#                     w.color = "BLACK"
#                     x.parent.color = "RED"
#                     self.left_rotate(x.parent)
#                     w = x.parent.right
                
#                 if self.is_black(w.left) and self.is_black(w.right):
#                     # Случай 2: оба ребенка  черные поднимаем проблему на уровень выше чтобы дальшее решать рекурсивно
#                     w.color = "RED"
#                     x = x.parent
#                 else:
#                     if self.is_black(w.right):
#                         # Случай 3: правый ребенок черный
#                         w.left.color = "BLACK"
#                         w.color = "RED"
#                         self.right_rotate(w)
#                         w = x.parent.right
                    
#                     # Случай 4: правый ребенок красный Окончательное исправление баланса
#                     w.color = x.parent.color
#                     x.parent.color = "BLACK"
#                     w.right.color = "BLACK"
#                     self.left_rotate(x.parent)
#                     x = self.root
#             else:
#                 # Симметричный случай, когда x является правым ребенком
#                 w = x.parent.left  # ребенок x
                
#                 if self.is_red(w):
#                     # Случай 1: ребенок красный
#                     w.color = "BLACK"
#                     x.parent.color = "RED"
#                     self.right_rotate(x.parent)
#                     w = x.parent.left
                
#                 if self.is_black(w.right) and self.is_black(w.left):
#                     # Случай 2: оба ребенка черные
#                     w.color = "RED"
#                     x = x.parent
#                 else:
#                     if self.is_black(w.left):
#                         # Случай 3: левый ребенок черный
#                         w.right.color = "BLACK"
#                         w.color = "RED"
#                         self.left_rotate(w)
#                         w = x.parent.left
                    
#                     # Случай 4: левый ребенок красный
#                     w.color = x.parent.color
#                     x.parent.color = "BLACK"
#                     w.left.color = "BLACK"
#                     self.right_rotate(x.parent)
#                     x = self.root
        
#         x.color = "BLACK"
    
#     def delete(self, key):
#         # Ищем узел для удаления
#         check = self.root
#         while check != self.list:
#             if key == check.key:
#                 break
#             elif key < check.key:
#                 check = check.left
#             else:
#                 check = check.right
        
#         if check == self.list:
#             return "KEY NOT FOUND"  # узел не найден
        
#         y = check
#         y_original_color = y.color
#         x = self.list
        
#         if check.left == self.list:
#             x = check.right
#             self.transplant(check, check.right)
#         elif check.right == self.list:
#             x = check.left
#             self.transplant(check, check.left)
#         else:
#             y = self.minimum(check.right)
#             y_original_color = y.color
#             x = y.right
            
#             if y.parent == check:
#                 x.parent = y
#             else:
#                 self.transplant(y, y.right)
#                 y.right = check.right
#                 y.right.parent = y
            
#             self.transplant(check, y)
#             y.left = check.left
#             y.left.parent = y
#             y.color = check.color
        
#         # Если удаленный узел был черным, восстанавливаем свойства
#         if y_original_color == "BLACK":
#             self.delete_fixup(x)
        
#         return None
    
#     def minimum(self, node):
#         # поиск минимума для правильного удаления
#         while node.left != self.list:
#             node = node.left
#         return node
    
#     def search(self, key):
#         # поиск узла по ключу
#         current = self.root
#         while current != self.list:
#             if key == current.key:
#                 return current
#             elif key < current.key:
#                 current = current.left
#             else:
#                 current = current.right
#         return None
    
#     def count_colors(self, node):
#         # рекурсивно считаю кол-во черных и красных узлов
#         if node == self.list:
#             return
        
#         if node.color == "RED":
#             self.red_count += 1
#         else:
#             self.black_count += 1
#         self.count_colors(node.left)
#         self.count_colors(node.right)

#     def get_color_counts(self):
#         #    кол-во красных и черных ключей
#         self.red_count = 0
#         self.black_count = 0
#         self.count_colors(self.root)
#         return self.red_count, self.black_count
    
#     def add(self, key, value): # добавление
#         return self.insert(key, value)
    
#     def lookup(self, key): # поиск по ключу
#         node = self.search(key)
#         if node:
#             return node.value
#         return "KEY NOT FOUND"
    
#     def delete_key(self, key): # удаление узла
#         return self.delete(key)
    
#     def print_rotations(self): # кол-во повротов 
#         return self.rotation_count
    
#     def print_count_black_keys(self): # кол-во черных ключей
#         red, black = self.get_color_counts()
#         return black
    
#     def print_count_red_keys(self): #  кол-во красных ключей
#         red, black = self.get_color_counts()
#         return red

# import sys
# input = sys.stdin.read
# data = input().splitlines()
# n = int(data[0])
# tree = RedBlackTree()
# results = []
# for i in range(1, n + 1):
#     command = data[i].split()
#     cmd_type = command[0]
#     if cmd_type == "ADD":
#         result = tree.add(int(command[1]), int(command[2]))
#         if result:
#             results.append(result)
#     elif cmd_type == "LOOKUP":
#         result = tree.lookup(int(command[1]))
#         results.append(str(result))
    
#     elif cmd_type == "DELETE":
#         result = tree.delete_key(int(command[1]))
#         if result:
#             results.append(result)
#     elif cmd_type == "PRINT_ROTATIONS":
#         result = tree.print_rotations()
#         results.append(str(result))
#     elif cmd_type == "PRINT_COUNT_BLACK_KEYS":
#         result = tree.print_count_black_keys()
#         results.append(str(result))
#     elif cmd_type == "PRINT_COUNT_RED_KEYS":
#         result = tree.print_count_red_keys()
#         results.append(str(result))
# for i in results:
#     print(i)

# def f(x=67):
#     if x <= 1:
#         return x
#     if x == 2:
#         return 2
#     if x == 3:
#         return 4
    
#     # Итеративное вычисление для максимальной производительности
#     a, b = 2, 4  # f(2) и f(3)
#     for i in range(4, x + 1):
#         a, b = b, a + b + 1
    
#     return b

# print(f())

print(2**( 32.5  )-1)