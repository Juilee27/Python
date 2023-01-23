'''
Problem: Check if two arrays are equal or not

https://practice.geeksforgeeks.org/problems/check-if-two-arrays-are-equal-or-not3847/1?page=1&difficulty[]=-1&curated[]=1&sortBy=submissions
'''

# approach:
# 1. Simply sort both arrays. If both match, return True.

# checking if sorted A and sorted B are matching.
def check(self,A,B,N):
        if sorted(A) == sorted(B):
            return True