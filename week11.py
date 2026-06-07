# # k.povasin@innopolis.university
# # идея решния была взята с лекции неделя 13 слайд 8
# import sys
# import random   
# N = int(input())
# alpha = ['A','B','C','D']
# random.shuffle(alpha)
# pref = ''
# for i in range(N):
#     for sym in alpha:
#         current = pref + sym
#         print("?" , current)
#         sys.stdout.flush()
#         entry = input()
#         if entry == 'Yes':
#             pref = current
#             break
#         else:
#             continue
# print("!", pref)
# sys.stdout.flush()

# k.povasin@innopolis.university
# идея решния была взята с лекции неделя 13 слайд 26
import random  
N = int(input())
A, B, C = [], [], []

def entry(sym):
    for _ in range(N):
        data = input()
        sym.append(list(map(int, data.split())))

entry(A)
entry(B)
entry(C)
# основная формула A*Br = Cr
k = 0
while k < 5: 
    r = [random.randint(0,1) for _ in range(N)] #бинарный вектор
    Br = []
    for stroka in range(N):
        sum_ = 0
        for stolbec in range(N):
            sum_ += B[stroka][stolbec] * r[stolbec]
        Br.append(sum_)
    
    ABr = []
    for stroka in range(N):
        sum_ = 0
        for stolbec in range(N):
            sum_ += A[stroka][stolbec] * Br[stolbec]
        ABr.append(sum_)
    
    Cr = []
    for stroka in range(N):
        sum_ = 0
        for stolbec in range(N):
            sum_ += C[stroka][stolbec] * r[stolbec]
        Cr.append(sum_)
    
    if ABr != Cr:
        print('No')
        exit()  
    k += 1
print('Yes')




