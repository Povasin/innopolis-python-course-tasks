# import random
# import sys
# # Используем быстрый ввод
# input_data = sys.stdin.read().split()
# ptr = 0
# N = int(input_data[ptr]); ptr += 1
# Q = int(input_data[ptr]); ptr += 1
# fitness = []
# for _ in range(N):
#     name = input_data[ptr]; ptr += 1
#     price = int(input_data[ptr]); ptr += 1
#     fitness.append((name, price))

# def Best(i, pivot):
#     if i[1] < pivot[1]:
#         return True
#     elif i[1] == pivot[1] and i[0] > pivot[0]:
#         return True
#     else:
#         return False

# def RandomiseParttion(mass, p, r):
#     i = random.randint(p, r) #получаем случайно опорный элемент
#     temp = mass[i]
#     mass[i], mass[r] = mass[r], mass[i]
#     pivot = mass[r]
#     last_smaller = p - 1
#     for j in range(p,r):
#         if Best(mass[j], pivot):
#             last_smaller +=1
#             mass[last_smaller], mass[j] = mass[j], mass[last_smaller]
#     # ставлю пивот на нужное место
#     mass[last_smaller + 1], mass[r] = mass[r], mass[last_smaller + 1]
#     return last_smaller+1
# # ищем k порядковую статистику в диапазоне [p, r]
# def Randomise_select(mass, p,r,k):
#     # база рекурсии если диапазон еденичный возращаем индекс текущий
#     if p == r:
#         return mass[p]
#     q = RandomiseParttion(mass,p,r) #получаем опорный элемент
#     positionCurrent = q - p + 1 #получаем индекс относитьльно тексущего массива
#     if k == positionCurrent:            #нашли 
#         return mass[q]
#     elif k < positionCurrent:      
#         return Randomise_select(mass, p, q-1, k) #рекурсивно ищем в левой части
#     else:               
#         return Randomise_select(mass, q+1, r, k-positionCurrent) #рекурсивно ищем в правой части
    
# for item in range(Q):
#     L = int(input_data[ptr]); ptr += 1
#     R = int(input_data[ptr]); ptr += 1
#     k = int(input_data[ptr]); ptr += 1
#     result = Randomise_select(fitness[L-1:R], 0, len(fitness[L-1:R]) - 1,k)
#     print(f"{result[1]} {result[0]}")

import sys
import random
class Node:
    def __init__(self, name, pages):
        self.name = name
        self.pages = pages
        self.priority = random.random()
        self.left = None
        self.right = None
        self.size = 1

def get_size(node):
    return node.size if node else 0

def update_size(node):
    if node:
        node.size = 1 + get_size(node.left) + get_size(node.right)
# вставка по страницам
def compare_nodes(pages1, pages2):
    return pages1 < pages2
# Разделение дерева по количеству страниц (ключу)
def split_by_pages(node, pages):
    if not node:
        return None, None
    if node.pages < pages:
        node.right, r = split_by_pages(node.right, pages)
        update_size(node)
        return node, r
    else:
        l, node.left = split_by_pages(node.left, pages)
        update_size(node)
        return l, node
# Разделение дерева по порядковому номеру (k)
def split_by_size(node, k):
    if not node:
        return None, None
    left_size = get_size(node.left)
    if left_size < k:
        node.right, r = split_by_size(node.right, k - left_size - 1)
        update_size(node)
        return node, r
    else:
        l, node.left = split_by_size(node.left, k)
        update_size(node)
        return l, node
def merge(l, r):
    if not l or not r:
        return l or r
    if l.priority > r.priority:
        l.right = merge(l.right, r)
        update_size(l)
        return l
    else:
        r.left = merge(l, r.left)
        update_size(r)
        return r
# Random select
def os_select(node, k):
    while node:
        left_size = get_size(node.left)
        if left_size + 1 == k:
            return node
        elif left_size >= k:
            node = node.left
        else:
            k -= (left_size + 1)
            node = node.right
    return None

input_data = sys.stdin.read().split()
ptr = 0
N = int(input_data[ptr]); ptr += 1
Q = int(input_data[ptr]); ptr += 1
root = None
# Начальное построение дерева
for _ in range(N):
    name = input_data[ptr]; ptr += 1
    pages = int(input_data[ptr]); ptr += 1
    new_node = Node(name, pages)
    l, r = split_by_pages(root, pages)
    root = merge(merge(l, new_node), r)
for _ in range(Q):
    query_type = input_data[ptr]; ptr += 1
    if query_type == "select":
        k = int(input_data[ptr]); ptr += 1
        res = os_select(root, k)
        print(f"{res.name} {res.pages}")
    elif query_type == "add":
        name = input_data[ptr]; ptr += 1
        pages = int(input_data[ptr]); ptr += 1
        new_node = Node(name, pages)
        l, r = split_by_pages(root, pages)
        root = merge(merge(l, new_node), r)
    elif query_type == "remove":
        k = int(input_data[ptr]); ptr += 1
        # Удаление k-й статистики через два сплита по размеру
        l, mid_r = split_by_size(root, k-1)
        target, r = split_by_size(mid_r, 1)
        root = merge(l, r)