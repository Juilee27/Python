'''
Problem: Find triplets with zero sum

https://practice.geeksforgeeks.org/problems/find-triplets-with-zero-sum/1?page=1&difficulty[]=-1&status[]=unsolved&sortBy=submissions

NOTE: ALL APPROACHES RETURN SINGLE TRIPLET RESULT AS WE are using return once we finding 3rd val.

approach 1 (mine): --- this is right but got TLE
1. as time complexity of n2 is allowed, using nested for loops to iterate and sum.
2. basic problem is to find triplets. Fix first 2 elements, iterate.
3. 3rd element is sum - (1st +2nd)
4. if 3rd in arr, return true
'''

'''
n = len(arr)
arr = [4 ,-16, 43, 4, 7, -36, 18]

def findTriplets(arr, n):
    #i to iterate from index 0 to n-2
    for i in range(n-1):
        #j to iterate from index i+1 to n-1
        for j in range(i+1, n):
            sum = arr[i]+arr[j]
            #expected sum is zero hence 0-sum. If sum has some other val, this will be val-sum here.
            third = 0-sum
            #Find third in arr. third shld not be arr[i] & arr[j] as we finding triplets with distinct vals.
            if third in arr and third != arr[i] and third != arr[j]:
                return 1
            
print(findTriplets(arr,n))
'''

'''
approach 2: SORTING ---------- this is right but got TLE
1. sort arr
2. take i - 1st element of arr, take j = i+1, k =last element
3. sum  = res - arr[i] = arr[j] + arr[k] --- check this
4. if arr[j] + arr[k] < sum, do j+=1
5. if arr[j] + arr[k] > sum, do k-=1
'''
'''
arr = [4 ,-16, 43, 4, 7, -36, 18]
n = len(arr)

def findTriplets(arr, n):
    arr.sort()  #sort arr.
    #i to iterate from 0 to n-3 index.
    for i in range(n-2):
        m = 0 - arr[i]  #if some other  sum value, replace 0 with sum
        j=i+1
        k = n-1
        while j<k:
            if arr[j] + arr[k] == m:
                return 1
            elif arr[j] + arr[k] <m:
                j+=1
            elif arr[j] + arr[k] >m:
                k-=1
    return 0
print(findTriplets(arr,n))
'''

'''
approach 3: tweaked the above one , logic is same
'''
'''
# arr = [4 ,-16, 43, 4, 7, -36, 18]
arr = [1,-2,1,7]
n = len(arr)
def findTriplets(arr, n):
    arr.sort()
    for i in range(n-2):
        j=i+1
        k = n-1
        while j<k:
            s = arr[i]+arr[j]+arr[k]
            if s == 0:
                return 1
            elif s < 0: ##if some other sum value, replace 0 with sum
                j+=1
            else:
                k-=1
    return 0
print(findTriplets(arr,n))
'''

'''
approach 4: using set
1. use i and j, 2 loops, nested
2. if sum - (arr[i] + arr[j]) is element in set return true
3. else add arr[j] to set, *set will contain unique vals.
'''
# arr = [4 ,-16, 43, 4, 7, -36, 18]
arr = [1,0,0,-2,1,0,0,0,7]
n = len(arr)
def findTriplets(arr, n):
    s1 = set()
    for i in range(n-1):
        for j in range(i+1, n):
            m = 0 - (arr[i]+arr[j])
            #check if m in s1
            if m in s1:
                return 1
            #if not in s1, add arr[j] to s1 set.
            else:
                s1.add(arr[j])
    return 0            

print(findTriplets(arr,n))