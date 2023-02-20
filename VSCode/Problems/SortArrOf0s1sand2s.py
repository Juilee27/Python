'''
Problem: Sort an array of 0s, 1s and 2s.

https://practice.geeksforgeeks.org/problems/sort-an-array-of-0s-1s-and-2s4231/0

approach:
1. simply return sorted array.
'''
arr = [0 ,2, 1, 2, 0, 2, 1]
N = len(arr)

def sort012(arr,n):        
    return arr.sort()

#approach 2: count no of 0's, 1's and 2's in arr and create new arr consisting of these counts.
def sort012(arr,n):
    arr=[0]*arr.count(0)+[2]*arr.count(2)+[1]*arr.count(1)
    return arr

# approach 3: iterate arr. swap 0's and 2's. do not swap 1's keep them at the same place.
#User function Template for python3

def sort012(arr,n):
        lo=0
        mid=0
        hi =n-1
        while mid<=hi:
            if arr[mid]==0:
                arr[lo],arr[mid]=arr[mid],arr[lo]  #swapping
                lo+=1
                mid+=1
            elif arr[mid]==1:
                mid+=1
            elif arr[mid]==2:
                arr[mid],arr[hi]=arr[hi],arr[mid]  #swapping
                hi -=1
