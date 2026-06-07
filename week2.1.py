# import sys
# data = list(map(int, sys.stdin.read().strip().split()))
# p, q, r, s = data[:4]
# if q != r:
#     print(-1)
#     sys.exit()
# idx = 4
# A = [data[idx+i*q:idx+(i+1)*q] for i in range(p)]
# idx += p*q
# B = [data[idx+i*s:idx+(i+1)*s] for i in range(r)]

# # доводем до квадратной матрицы и до степени двойки
# n = max(p, q, s)
# m = 1
# while m < n:
#     m *= 2

# def pad_matrix(M, size):
#     rows = len(M)
#     cols = len(M[0])
#     new_M = [[0]*size for _ in range(size)]
#     for i in range(rows):
#         for j in range(cols):
#             new_M[i][j] = M[i][j]
#     return new_M

# A_pad = pad_matrix(A, m)
# B_pad = pad_matrix(B, m)


# # вспомаготельные функции 
# def plus(A, B):
#     n = len(A)
#     return [[A[i][j] + B[i][j] for j in range(n)] for i in range(n)]

# def minus(A, B):
#     n = len(A)
#     return [[A[i][j] - B[i][j] for j in range(n)] for i in range(n)]

# def split(M):
#     n = len(M)
#     mid = n // 2
#     A11 = [row[:mid] for row in M[:mid]]
#     A12 = [row[mid:] for row in M[:mid]]
#     A21 = [row[:mid] for row in M[mid:]]
#     A22 = [row[mid:] for row in M[mid:]]
#     return A11, A12, A21, A22

# def group(C11, C12, C21, C22):
#     top = [C11[i] + C12[i] for i in range(len(C11))]
#     bottom = [C21[i] + C22[i] for i in range(len(C21))]
#     return top + bottom
# # штрассен

# def strassen(A, B):
#     n = len(A)

#     if n == 1:
#         return [[A[0][0] * B[0][0]]] #база рекурсии если матрица 1

#     A11, A12, A21, A22 = split(A)
#     B11, B12, B21, B22 = split(B)

#     S1 = minus(B12, B22)
#     S2 = plus(A11, A12)
#     S3 = plus(A21, A22)
#     S4 = minus(B21, B11)
#     S5 = plus(A11, A22)
#     S6 = plus(B11, B22)
#     S7 = minus(A12, A22)
#     S8 = plus(B21, B22)
#     S9 = minus(A11, A21)
#     S10 = plus(B11, B12)

#     P1 = strassen(A11, S1)
#     P2 = strassen(S2, B22)
#     P3 = strassen(S3, B11)
#     P4 = strassen(A22, S4)
#     P5 = strassen(S5, S6)
#     P6 = strassen(S7, S8)
#     P7 = strassen(S9, S10)

#     C11 = plus(minus(plus(P5, P4), P2), P6)
#     C12 = plus(P1, P2)
#     C21 = plus(P3, P4)
#     C22 = minus(minus(plus(P5, P1), P3), P7)

#     return group(C11, C12, C21, C22)

# C_pad = strassen(A_pad, B_pad)
# # обрезаем
# for i in range(p):
#     print(*C_pad[i][:s])


N = int(input())
matrices = [list(map(int, input().split())) for _ in range(N)]
for i in range(0,N-1):
    if matrices[i][1] != matrices[i+1][0]:
        print("-1")
        exit()

dp = [[0] * N for _ in range(N)]
# Формируем массив размеров
dims = [matrices[0][0]]
for p, q in matrices:
    dims.append(q)
for length in range(2, N + 1):  # от 2 до N
    for i in range(N - length + 1):
        j = i + length - 1
        dp[i][j] = 100000000 # заглушка
        for k in range(i, j):
            cost = (
                dp[i][k]
                + dp[k + 1][j]
                + dims[i] * dims[k + 1] * dims[j + 1]
            )
            if cost < dp[i][j]:
                dp[i][j] = cost

print(dp[0][N - 1]) 