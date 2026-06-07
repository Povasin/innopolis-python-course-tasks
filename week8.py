# # k.povasin@innopolis.university
# # Идея решения была взята из лекции неделя 8 слайд 15
# MOD = 10**9 + 7
# N, K = map(int, input().split())
# mass = [0] * (N + 1)
# mass[1] = 1
# qount = mass[1]
# for i in range(2, N + 1):
#     mass[i] = qount
#     qount = (qount + mass[i]) % MOD
#     if i >= K:
#         qount = (qount - mass[i - K]) % MOD
# print(mass[-1])

# k.povasin@innopolis.university
# Идея решения была взята из лекции неделя 8 слайд 25
n = int(input())
mass = list(map(int, input().split()))
dp = [[0]*n for i in range(n)]
for i in range(n):
    dp[i][i] = mass[i] * n
for length in range(2, n + 1):
    for l in range(0, n-length+1):
        r = l+length-1
        year = n-(r-l)
        left=mass[l]*year+dp[l+1][r]
        right=mass[r]*year+dp[l][r-1]
        dp[l][r] = max(left, right)
print(dp[0][n-1])


def bestTime(N,T,O):
    dp = [ [0]*T for _ in range(N) ]
    bread = [ [0]*T for _ in range(N) ]
    for task in range(1,T):
        for note in range(T,N):
            bestTimeHere = 10**5
            bestUsel = 0
            for usel in range(note-(task-1)):
                check = dp[task-1][note-usel] + O[task][note] 
                if check < bestTimeHere:
                    bestTimeHere = check
                    bestUsel = usel
                dp[task][note] = bestTimeHere
                bread = bestUsel
    result = []
    for task in range(T,1,-1):
        ost=N
        bread[task][ost]
        result.append(bread[task][N])
        ost-=bread[task][ost]
    return (dp[T][N], result)
