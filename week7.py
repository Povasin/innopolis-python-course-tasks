# Кирилл Повасин k.povasin@innopolis.university
# Идея решения была взята из лекции 7 по алгоритмам слайд 30: 
# n = int(input())
# mass = [list(map(float, input().split())) for _ in range(n)]
# tempMass = [[] for _ in range(n + 1)]
# for i in range(n):
#     index = int((mass[i][0]**2 + mass[i][1]**2) * n)
#     if index > n:
#         index = n
#     tempMass[index].append(mass[i])
# for i in range(n + 1):
#     if len(tempMass[i]) > 1:
#         for j in range(1, len(tempMass[i])):
#             key = tempMass[i][j]
#             p = j - 1
#             while p >= 0 and (key[0]**2 + key[1]**2) < (tempMass[i][p][0]**2 + tempMass[i][p][1]**2):
#                 tempMass[i][p + 1] = tempMass[i][p]
#                 p -= 1
#             tempMass[i][p + 1] = key
# for i in tempMass:
#     for j in i:
#         print(f"{j[0]:.4f} {j[1]:.4f}")
        

# Кирилл Повасин k.povasin@innopolis.university
# Идея решения была взята из лекции 7 по алгоритмам слайд 20: 
n = int(input())
mass = [list(map(int, input().split())) for _ in range(n)]
mx = max(item[0] for item in mass)
tempmass = [[] for _ in range(mx + 1)]
for i in range(n):
    tempmass[mass[i][0]].append((mass[i][1], i+1))
res = []
for p in range(mx, -1, -1):
    tm = tempmass[p]
    if not tm:
        continue
    for i in range(1, len(tm)):
        key = tm[i]
        j = i-1
        while j >= 0 and tm[j][0] > key[0]:
            tm[j + 1] = tm[j]
            j -= 1
        tm[j+1] = key
    for item in tm:
        res.append(item[1])
print(*res)