'''
Problem: Leaders in an array

https://practice.geeksforgeeks.org/problems/leaders-in-an-array-1587115620/1?page=1&difficulty[]=0&curated[]=1&sortBy=submissions
'''
'''
approach 1:
1. if N=1, return A[0]
2. traverse arr, find max of no right to current A[i]. If current no is less than max_no, delete it from copy of arr. Return arr copy.
'''
A = [31, 40, 93, 40, 98]
# A=[1,2,3,4,0]
N = len(A)

# following approach by me - TLE.
# def leaders(A,N):
#     if N==1:
#         return A

#     ls= []
#     #1st find max of A
#     max_no = max(A)
#     #add in ls
#     ls.append(max_no)
#     j = A.index(max_no)
#     while j in range(j, N):
#         # find max of elements right to max_no
#         max_no= max(A[j:])
#         #add max to ls
#         ls.append(max_no)
#         #next range must start from elements right to max_no
#         j = A.index(max_no)+1
#     for z in ls:
#         cnt = ls.count(z)
#         #to remove repeated elements from ls
#         while cnt>1:
#             ls.remove(z)
#             cnt-=1
#     return ls
# print(leaders(A,N))

#following approach by me - TLE. it is same as previous one.
# def leaders(A, N):
#     #creating copy of A, as want to iterrate over A and not change it.
#     b = A.copy()
#     for i in range(N):
#         #as we want to keep last element, exit loop when last index comes.
#         if i != (N-1):
#             #find max of elements right to A[i]
#             max_no = max(A[i+1: N])
#             #if current A[i] is less than max_no remove it from b
#             if A[i] < max_no:
#                 b.remove(A[i])
#     return b
# print(leaders(A,N))

'''following is right soln.
approach 2: 
1. traverse A from right to left. A[i] is initial max_no.
2. add max_no to ls list. If next element is greater than max_no it is new max_no. 
'''
def leaders(A,N):
    ls=[]
    max_no = 0
    # ls.append(max_no)
    for i in range(-1, -(N+1), -1):
        if A[i] >= max_no:
            max_no = A[i]
            ls.append(max_no)
    return ls[::-1] #or can use reverse() func here

print(leaders(A,N))
