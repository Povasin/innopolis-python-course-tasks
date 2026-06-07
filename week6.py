# N, M = map(int, input().split())
# mount = [list(map(int, input().split())) for x in range(N)]
# def checkSavePlace(rowStart=0, rowEnd=N-1, colStart=0, colEnd=M-1):
#     if rowStart == rowEnd and colStart == colEnd:
#         return rowStart+1, colStart+1
#     if rowEnd+rowStart >= colEnd+colStart:
#         midRow = (rowStart+rowEnd)//2
#         minCol = colStart
#         for i in range(colStart, colEnd+1):
#             if mount[midRow][i] < mount[midRow][minCol]:
#                 minCol=i
#         if midRow > rowStart and mount[midRow-1][minCol] < mount[midRow][minCol]:
#             return checkSavePlace(rowStart, midRow-1, colStart, colEnd)
#         elif midRow < rowEnd and mount[midRow+1][minCol] < mount[midRow][minCol]:
#             return checkSavePlace(midRow+1, rowEnd, colStart, colEnd)
#         else:
#             return midRow+1, minCol+1
#     else:
#         midCol = (colStart+colEnd)//2
#         minRow = rowStart
#         for i in range(rowStart, rowEnd+1):
#             if mount[i][midCol] < mount[minRow][midCol]:
#                 minRow=i
#         if midCol > colStart and mount[minRow][midCol-1] < mount[minRow][midCol]:
#             return checkSavePlace(rowStart, rowEnd, colStart, midCol-1)
#         elif midCol < colEnd and mount[minRow][midCol+1] < mount[minRow][midCol]:
#             return checkSavePlace(rowStart, rowEnd, midCol+1, colEnd)
#         else:
#             return minRow+1, midCol+1
# print(*checkSavePlace())


def separateMass(mass,k):
    if len(mass) <= k:
        for i in range(k):
            key = mass[i]
            j = i
            while j > 0 and mass[j-1] > key:
                mass[j] = mass[j-1]
                j -= 1
            mass[j] = key
        return mass
    left_sorted = separateMass(mass[:len(mass)//2:],k)
    right_sorted = separateMass(mass[len(mass)//2::],k)
    return connectMass(left_sorted, right_sorted)   
def connectMass(left, right):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i+=1
        elif left[i] > right[j]:
            result.append(right[j])
            j+=1
    while i<len(left):
        result.append(left[i])
        i+=1
    while j<len(right):
        result.append(right[j])
        j+=1
    return result


# N = int(input())
# process = []
# for _ in range(N):
#     data = input().split()
#     process.append([int(data[0]), data[1]])
# def sortMass(mass, inx=(N-1)//2):
#     if len(mass) == 1:
#         return mass[0]
#     pivot = mass[len(mass)//2]
#     left = [x for x in mass if x[0] < pivot[0]]
#     right = [x for x in mass if x[0] > pivot[0]]
#     mid = [x for x in mass if x[0] == pivot[0]]
#     if inx < len(left):
#         return sortMass(left, inx)
#     elif inx == len(left):
#         return mid[0]
#     else:
#         return sortMass(right, inx-len(left)-len(mid))
# print(sortMass(process)[1])
