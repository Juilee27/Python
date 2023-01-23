'''
Problem : Print 1 to n without using loops

https://practice.geeksforgeeks.org/problems/print-1-to-n-without-using-loops3621/1?page=2&difficulty[]=-2&sortBy=submissions

Note : range() returns iterable range object. This iterable can be unpacked (using *args) and used.
'''
# Steps:
# 1. Can use recursion or range func for this task.
# 2. Let's go with Printing this using range func. Easiest way.

class Solution:
    def printTillN(self, N):
    	# print(*range(1,N+1),end="")  #this is using range

        if N>0:        #this is using recursion.
            self.printTillN(N-1)
            print(N,end=" ")

ob = Solution()
ob.printTillN(5)

# s = "".join(map(str, range(1, n + 1)))
# print(s)
