# n = int(input())
# MassLines = ['' for x in range(n)]
# class lastOpenSym:
#     def __init__(self):
#         self.size = 0
#         self.items = [['', 0, 0] for x in range(10)]
#     def add(self,obj):
#         self.items[self.size] = obj 
#         self.size +=1
#     def get(self):
#         return self.items[self.size-1]
#     def remove(self):
#         self.size -=1   
#         self.items[self.size] = ['', 0,0] 
# checkobj = {'(': ')', '[':']', '{':'}', '}':'{', ')':'(', ']':'['}
# l = lastOpenSym()
# def checkFunc(open,line,col):
#     global MassLines
#     if l.get()[0] != open:
#         if l.get()[0] == '[' or l.get()[0] == '(' or l.get()[0] == '{':
#             print(f"Error in line {line+1}, column {col+1}: expected '{checkobj[l.get()[0]]}', but got '{MassLines[line][col]}'.")
#             exit()
#     l.remove()
# for i in range(n):
#     MassLines[i] = input()
# for line in range(len(MassLines)):
#     for col in range(len(MassLines[line])):
#         if (l.get()[0] == '') and (MassLines[line][col] == ')' or MassLines[line][col] == ']' or MassLines[line][col] == '}'):
#             print(f"Error in line {line+1}, column {col+1}: unexpected closing '{MassLines[line][col]}'.")
#             exit()
#         if  MassLines[line][col] == '(' or MassLines[line][col] == '[' or MassLines[line][col] == '{':
#             l.add([MassLines[line][col], line, len(MassLines[line])])
#         if  MassLines[line][col] == ')' or MassLines[line][col] == ']' or MassLines[line][col] == '}':
#             checkFunc(checkobj[MassLines[line][col]],line,col)
# if l.get()[0]  != '':
#         print(f"Error in line {l.get()[1]+1}, column {l.get()[2]}: expected '{checkobj[l.get()[0]]}', but got end of input.")
#         exit()
# print("Input is properly balanced.")  

# n = int(input())
# class orderCl:
#     def __init__(self):
#         self.size = 0
#         self.sizeResult = 0
#         self.beginning = 0
#         self.items = [None] *n
#         self.result = [None] *n
#     def top(self):
#         if self.beginning >= self.size:
#             self.result[self.sizeResult] = ['Empty']
#         else:
#             self.result[self.sizeResult] = self.items[self.beginning]
#         self.sizeResult += 1
#     def add(self, obj):
#         self.items[self.size] = obj
#         self.size+=1
#     def proceed(self):
#         if self.beginning < self.size:
#             self.beginning+=1
#     def get(self):
#         for i in range(self.sizeResult):
#             print(*self.result[i])
# order = orderCl()
# for i in range(n):
#     command = input().split()
#     if command[0] == 'Add': 
#         order.add((command[1],command[2],command[3],command[4]))
#     if command[0] == 'Top':
#         order.top()
#     if command[0] == 'Proceed':
#         order.proceed()
# order.get()

# def func(n):
#     class Node:
#         def __init__(self, value, next):  
#             self.value = value            
#             self.next = next  
#     class LinkedList:
#         def __init__(self):
#             self.size = 0
#             self.head = None    
#         def reverse(self):
#             cur = self.head
#             before = None
#             while cur.next:
#                 temp = cur
#                 cur.next = before
#                 before = cur
#                 cur = temp
#             self.head = before
#             return before


# class order:
#     def __init__(self):
#         self.sizeStackAdd = 0
#         self.sizeStackDelete = 0 
#         self.stackAdd = [None]*n            
#         self.stackDelete = [None]*n
#     def size(self):
#         return self.sizeStackAdd+self.sizeStackDelete
#     def is_empty(self):
#         return  (order.size() == 0)
      
#     def offer(self,x):
#         self.stackAdd[self.sizeStackAdd] = x
#         self.sizeStackAdd += 1
#     def poll(self):
#         if order.is_empty():
#             while self.sizeStackAdd != 0:
#                 self.stackDelete[self.sizeStackDelete] = self.stackAdd[self.sizeStackAdd-1]
#                 self.sizeStackDelete+=1
#                 self.sizeStackAdd-=1
#             self.sizeStackDelete-=1
#             return  self.stackDelete[self.sizeStackDelete]
#         else:
#             return 'Очередь пустая'
#     def peek(self):
#         if order.is_empty():
#             return order.poll()
#         else:
#             return 'Очередь пустая'

               
         



    
