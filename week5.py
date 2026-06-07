# N = int(input())
# massTrain = [ (input().split())for x in range(N)]
# Q = int(input())
# result = [(0, None, None) for x in range(Q)]
# index = 0
# for x in range(Q):
#     data = input().split()
#     if data[0] == 'Report':
#         if massTrain:
#             result[index] = (len(massTrain), massTrain[0], massTrain[-1])
#         index+=1
#     elif data[0] == 'Connect':
#         if data[1] == 'left':
#             massTrain.insert(0,data[2:])
#         else:
#             massTrain.append(data[2:])
#     elif data[0] == 'Disconnect' and massTrain:
#         if data[1] == 'left':
#             massTrain.pop(0)
#         else:
#             massTrain.pop()
# for i in range(index):
#     print(result[i][0])
#     if result[i][1]:
#         print(*result[i][1])
#     if result[i][2]:
#         print(*result[i][2])

# N,M = map(int, input().split())
# result = list( input().split() for x in range(N))
# massPole = [list(row[0]) for row in result]
# countStar = sum(x.count('S') for x in massPole)
# if countStar > N+M-1:
#     print(0)
#     exit()
# if massPole[0][0] == '#':
#     print(0)
#     exit()
# cash = {}
# def comPole(x=0, y=0, coll=0):
#     if x >= M or y >= N or massPole[y][x] == '#':
#         return 0
#     curStar = coll
#     if massPole[y][x] == 'S':
#         curStar += 1
#     if x == M-1 and y == N-1:
#         if curStar==countStar:
#             return 1
#         else:
#             return 0
#     if (x, y, curStar) in cash:
#         return cash[(x, y, curStar)]
#     result = comPole(x+1, y, curStar) + comPole(x, y+1, curStar)
#     cash[(x, y, curStar)] = result
#     return result
# print(comPole())

N = int(input())
massTrain = [input().split() for x in range(N)]
Q = int(input())
result = []
index = 0
leftStack = []
rightStack = massTrain[:]
for x in range(Q):
    data = input().split()
    if data[0] == 'Report':
        size = len(leftStack) + len(rightStack)
        if size > 0:
            if leftStack:
                first = leftStack[-1]
            else:
                first = rightStack[0]
            if rightStack:
                last = rightStack[-1]
            else:
                last = leftStack[0]
            result.append((size, first, last))
        else:
            result.append((0, None, None))
        index += 1
    elif data[0] == 'Connect':
        if data[1] == 'left':
            leftStack.append(data[2:])
        else:
            rightStack.append(data[2:])
    elif data[0] == 'Disconnect':
        size = len(leftStack) + len(rightStack)
        if size > 0:
            if data[1] == 'left':
                if leftStack:
                    leftStack.pop()
                elif rightStack:
                    leftStack = rightStack[:len(rightStack) //2][::-1]
                    rightStack = rightStack[len(rightStack) // 2:]
                    if leftStack:
                        leftStack.pop()
            else:
                if rightStack:
                    rightStack.pop()
                elif leftStack:
                    rightStack = leftStack[:len(leftStack) //2][::-1]
                    leftStack = leftStack[len(leftStack) // 2:]
                    if rightStack:
                        rightStack.pop()
for i in range(index):
    print(result[i][0])
    if result[i][1]:
        print(*result[i][1])
    if result[i][2] and result[i][0] > 1:
        print(*result[i][2])


# N, M = map(int, input().split())
# result = list(input().split() for x in range(N))
# massPole = [list(row[0]) for row in result]
# countStar = sum(x.count('S') for x in massPole)
# if countStar > N + M - 1:
#     print(0)
#     exit()
# if massPole[0][0] == '#':
#     print(0)
#     exit()
# cash = [[[None]*(countStar+1) for i in range(N)] for j in range(M)]
# def comPole(x=0, y=0, coll=0):
#     if x >= M or y >= N or massPole[y][x] == '#':
#         return 0
#     curStar = coll
#     if massPole[y][x] == 'S':
#         curStar += 1
#     if x == M - 1 and y == N - 1:
#         if curStar == countStar:
#             return 1
#         else:
#             return 0
#     if cash[x][y][curStar] != None:
#         return cash[x][y][curStar]
#     result = comPole(x + 1, y, curStar) + comPole(x, y + 1, curStar)
#     cash[x][y][curStar] = result
#     return result
# print(comPole())


N = int(input())
massTrain = [input().split() for x in range(N)]
Q = int(input())
result = []
leftStack = []
rightStack = massTrain[:]
for x in range(Q):
    data = input().split()
    
    if data[0] == 'Report':
        size = len(leftStack) + len(rightStack)
        if size == 0:
            result.append((0, None, None))
        else:
            if leftStack:
                first = leftStack[-1]
            else:
                first = rightStack[0]
            if rightStack:
                last = rightStack[-1]
            else:
                last = leftStack[0]
            result.append((size, first, last))
    elif data[0] == 'Connect':
        if data[1] == 'left':
            leftStack.append(data[2:])
        else: 
            rightStack.append(data[2:])
    elif data[0] == 'Disconnect':
        if data[1] == 'left':
            if leftStack:
                leftStack.pop()
            elif rightStack:
                rightStack.pop(0)
        else:
            if rightStack:
                rightStack.pop()
            elif leftStack:
                leftStack.pop(0)
for i in range(len(result)):
    print(result[i][0])
    if result[i][1] != None:
        print(*result[i][1])
    if result[i][2] != None and result[i][0] > 1:
        print(*result[i][2])