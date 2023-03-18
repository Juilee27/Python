'''
Problem: Peak element

https://practice.geeksforgeeks.org/problems/peak-element/1?page=1&status[]=unsolved&sortBy=submissions

approach:
1. find max of arr.
2. return index of max element.
'''

arr = [1,3,3]
n = len(arr)

# def peakElement(arr, n):
#     return arr.index(max(arr))

# print(peakElement(arr,n))

'''
approach 2: 
1. this is w/o using list functions.
    if len(arr) = 1 or first element is greater than 2nd element, return 0 index.
2. if last element is greater than 2nd last element, return last index. 
3. if some other index element is greater than its adjacent elements, return that index.
'''

def peakElement(arr,n):
    if n==1 or (arr[0] >= arr[1]):
        return 0
    elif arr[n-1] >= arr[n-2]:
        return n-1
    for i in range(1,n-1):
        if arr[i] >= arr[i+1] and arr[i] >= arr[i-1]:
            return i        
        
print(peakElement(arr,n))