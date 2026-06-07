# def make_mono(a):
#     k = 0
#     lastObj = 0
#     for i in range(len(a)-1):
#         if a[i] < a[i+1] and k > 0:
#             a[i-k] = a[i+1]
#             lastObj =  a[i-k]
#         else:
#             k+=1
#     return a, lastObj
# print(make_mono([2, 10, 4, 3, 5, 8]))

# def func(A,B,k):
#     fr = 0
#     while fr < B[0]:
#         sec= 0
#         checkRes = 1
#         for i in range(k-1):
#             sec+=B[i]
#             tempSec = sec
#             if A[fr] < A[sec]:
#                 while sec < tempSec + B[i+1]:
#                     if A[fr] == A[sec]:
#                         checkRes+=1
#                         break
#                     sec+=1
#             sec = tempSec
#         if checkRes == k:
#             print(A(fr))
#         fr+=1

# print(func([2,3,5,8,1,3,5,1,2,3,4,5], [4,3,5], 3))




