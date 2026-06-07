# Кирилл Повасин k.povasin@innopolis.university
# n,x = map(int, input().split())
# earn = list(map(int, input().split()))
# qount = [None]*(x+1)
# qount[0] = [0]*n
# for s in range(x):
#     if qount[s] != None:
#         for i in range(n):
#             summa = s+earn[i]
#             if summa <= x and qount[summa] == None:
#                 commbination = [x for x in qount[s]]
#                 commbination[i] += 1
#                 qount[summa] = commbination
#                 if summa == x:
#                     print("yes")
#                     print(*qount[x])
#                     exit()
# print("no")



# flag = True
                # for j in range(1,M):
                #     if pole[i+M+j] != None:
                #         flag = False
                #         break
                # if flag:
# elif pole[i]['x'] == 0 and pole[i]['y'] < M-1:
#     if pole[i+1]['person'] == None and pole[i+M]['person'] == None and pole[i+M-1]['person'] == None:
#         pole[i] = 'i'
#         tempI-=1
# elif pole[i]['x'] == 0 and pole[i]['y'] == M-1:
#     if pole[i-1]['person'] == None and pole[i+M]['person'] == None and pole[i+M-1]['person'] == None:
#         pole[i] = 'i'
#         tempI-=1
# elif pole[i]['x'] != 0 and pole[i]['y'] == 0:
#     if pole[i-M]['person'] == None and pole[i+M]['person'] == None and pole[i+1]['person'] == None:
#         flag = True
#         for k in range(1,max(M,N)):
#             if pole[i-k*M+k]['person'] != None and pole[i+k*M+k]['person'] != None:
#                 flag=False
#         if flag:
#             pole[i] = 'i'
#             tempI-=1

# Кирилл Повасин k.povasin@innopolis.university
# def cheked(pole,x,y):
#     flag=True
#     if x+1<N:
#         if pole[y][x+1] == 'i':
#             flag=False
#     if y+1<M:
#         if pole[y+1][x] == 'i':
#             flag=False
#     if y-1>=0:
#         if pole[y-1][x] == 'i':
#             flag=False
#     if x-1>=0:
#         if pole[y][x-1] == 'i':
#             flag=False
#     for k in range(1,max(M,N)):
#         if y+k<M and x+k<N:
#             if pole[y+k][x+k] == 'i':
#                 flag=False
#         if y+k<M and x-k>=0:
#             if pole[y+k][x-k] == 'i':
#                 flag=False
#         if y-k>=0 and x-k>=0:
#             if pole[y-k][x-k] == 'i':
#                 flag=False
#         if y-k>=0 and x+k<N:
#             if pole[y-k][x+k] == 'i':
#                 flag=False
#     return flag
# N,M,I,E = map(int, input().split())
# def addPerson(lastObj=[0,0],tempI=I,tempE=E,pole = [['.' for j in range(N)] for i in range(M)]):
#     if tempI != 0:
#         for y in range(0,M):
#             if tempI == 0:
#                 break
#             for x in range(0,N):
#                 if cheked(pole,x,y):
#                     if pole[y][x] != 'i':
#                         pole[y][x] = 'i'
#                         tempI-=1
#                 if tempI == 0:
#                     break
#     if tempI == 0:
#         if tempE != 0:
#             for y in range(M):
#                 if tempE == 0:
#                     break
#                 for x in range(N):
#                     if cheked(pole,x,y):
#                         if pole[y][x] != 'i':
#                             pole[y][x] = 'e'
#                             tempE-=1
#                     if tempE == 0:
#                         break
#         if tempE == 0:
#             print('possible')
#             for z in range(M):
#                 print(''.join(str(i) for i in pole[z]))
#             exit()
#         else:
#             tempI=I
#     if tempI != 0:
#         tempI=I
#         pole = [['.' for j in range(N)] for i in range(M)]
#         tempE=E
#         if indexforX < N:
#             indexforX+=1
#             addPerson(indexforX,indexforY,tempI,tempE,pole)
#         elif indexforY < M:
#             indexforX=0
#             indexforY+=1
#             addPerson(indexforX,indexforY,tempI,tempE,pole)
#         else:
#             print('impossible')
#             exit()
# addPerson()

# def cms(A, n, k, s):
#     if n < k:
#         return 0
#     elif k == 0:
#         return s
#     else:
#         m = n-1
#         for j in range(n):
#             if A[j] < A[m]:
#                 m = j
#         tmp = A[n]
#         A[n] = A[m]
#         A[m] = tmp
#         x = A[n]
#         a = cms(A, n - 1, k, s)
#         b = cms(A, n - 1, k - 1, s + x)
#         return max(a, b)
# print(cms([5,2,8,3],4, 3, 0))

# def cms_iterative(A, n, k, s):
#     stack = [[n, k, s, 0, None, None], [0, 0, 0,None,None] for x in range(n*k)]
#     res = [[0,0,0] for x in range(n*k)]
#     i = 0
#     while i<n*k:
#         n, k, s, step, m, x = stack[i]
#         if n < k:
#             return 0
#         if k == 0:
#             return s
#         if step == 0:
#             m = 0
#             for j in range(1,n):
#                 if A[j] < A[m]:
#                     m = j
#             A[m] = A[n-1]
#             A[n-1] = A[m]
#             stack[i] = [n, k, s, 1, m, A[n-1]]
#             stack[i+1]= [n-1, k, s, 0, None, None]
#         elif step == 1:
#             a = res[i]
#             stack[i]=[n,k,s,2,m,x]
#             stack[i+1] = [n-1, k-1, s + x, 0, None, None]
#         elif step == 2:
#             b = res[i]
#             a = res[i+1]
#             result = max(a, b)
#             res[[n, k, s]] = result
#         i+=1
#     return res

def nod(a):
    massDel = [a, None for x in range(a**0.5+1)]
    k=1
    for i in range(2,a**0.5+1):
        if a%i==0:
            massDel[k] = i
            k+=1
    return [massDel[i] for i in range(k)]     
def checked(A,n):
    qount = 0
    for i in range(n-1):
        res = nod(A[i]) + [None for x in range(1000)]
        for j in range(i+1,n):
            flag = True
            massNod = nod(A[j])
            for check in massNod:
                for tempRes in res:
                    if check == tempRes:
                        flag = False
                        break
            if flag:
                tempResIndex=1
                for massNodItem in massNod:
                    res[len(nod[A[i]])+tempResIndex] = massNodItem
                    tempResIndex+=1
                qount+=1  
    return qount
        