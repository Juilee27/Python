#Problem - Function to reverse every sub-array group of size K.
K = 3
arr = [1, 2, 3, 4, 5, 7, 8, 9]
N = len(arr)

# '''solution2: (Editorial solution)
l = 0
r = min(N, K)
str1 = ''
# while l < N:
#     arr[l:r] = arr[l:r][::-1]
#     l = l+K
#     r = min(N, r+K)
# print(arr)

#FOLLOWING IS THE BEST SOLUTION:
for r in range(0,N,K):
    # arr[r:r+K] = reversed(arr[r:r+K])
    arr[r:r+K] = arr[r:r+K][::-1] #this is same as line 18
print(arr)

'''my solution1: #Not optimal, TLE-Time Limit Exceeding
ans=''
for i in range(len(arr)//3):
    print(arr[K*i:K*(i+1)] ,end=' ')
    for n in range(3):
        ans+=  (str(arr[K*i:K*(i+1)][2-n])+' ')
ln = len(arr)%3  #if last elements remain
if ln != 0:
    for j in range(1,ln+1):
        # print(arr[-j] , end=' ')
        ans+= str(arr[-j])
print(ans)
'''

'''
Steps:
This is good example of list slicing.
1. divide seq in set of K. Use step in range() for this.
2. reverse every set. use list slicing for this
'''