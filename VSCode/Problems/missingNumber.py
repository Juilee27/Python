'''
Problem: Missing number

https://practice.geeksforgeeks.org/problems/missing-number4257/1?page=3&difficulty[]=-1&sortBy=latest
'''

'''
initial approach:
note - this has Time Limit Exceed (TLE). So cant use.
def missingNumber( A, N):
     # Your code goes here
    for i in range(1,N+1):
        if i not in A:
            return i 
'''


'''
approach 1:
HASHMAP:
1. take hashmap. put 1 to N in hashmap. Keep all values False initially. 
2. iterate over given arr. value that's present in hashmap, mark it TRUE.
3. return value that remains FALSE in hashmap.

N=5
A=[2, 5, 3, 1]

def missingNumber(A, N):
    hashmap = {}
    for i in range(1, N+1):
        hashmap[i] = False
    # print(hashmap)
    for j in A:
        if j in hashmap:
            hashmap[j]=True

    for key,val in (hashmap.items()):
        if val==False:
            return key

print(missingNumber(A,N))
'''

'''
approach 2:
1. sum of N natural nos = N(N+1)/2
2. sum of int in arr
3. Sn - Sarr is the missing num.
Note - This can have integer overflow issue if N is too big. Hence overflow condition needs to be taken care.

N=5
A=[2, 5, 3, 1]

def missingNumber(A, N):
    sum_N = N*(N+1)//2
    sum_arr = 0
    for i in A:
        sum_arr += i
    return (sum_N - sum_arr)

print(missingNumber(A,N))
'''

'''
approach 3:
1. perform XOR operation for elements of N and given arr. XOR is bitwise OR operation.
2. this gives missing element as repeated elements are cancelled in XOR.
'''
N=5
A=[2, 5, 3, 1]

def missingNumber(A, N):
    a=0
    b=0
    for i in A:
        a= a^i
    while N>0:
        b=b^N
        N-=1
    return a^b

print(missingNumber(A,N))