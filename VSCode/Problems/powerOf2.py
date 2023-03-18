'''
problem: Power of 2

https://practice.geeksforgeeks.org/problems/power-of-2-1587115620/1?page=1&difficulty[]=-1&status[]=unsolved&sortBy=submissions

N= 2^x

approach:
1. N=1 , return true
2. check if N%2 == 0. if yes do N//2
'''

# '''
N = 120
def isPowerofTwo(n):
    # ls=[]
    #this is 2^0.
    if n == 1:
        return True
    #if n is not even no or n =0.
    elif (n % 2 != 0) or n==0:  #mod returns int val.
        return False

    #if n is even.
    else:
        #NOTE - this fol list approach is TLE.
        # while n!=1:
        #     n = n //2
        #     ls.append(n)
        # for i in ls:
        #     if i!=1 and i%2==1:
        #         return False
        # return True

        #fol is smart approach.
        while n:
            #keep dividing n by 2.
            n= n//2
            #if n is some power 2, n's last val is gonna be 2 and 2//2=1. hence return True
            if n==1:
                return True
            #if remainder is not zero, its not power of 2.
            elif n%2 !=0:
                return False
'''

N=128
'''
# approach 2:
'''
def isPowerofTwo(n):
    return (bin(n))[2::].count('1')==1


'''
# approach 3:
'''
# def isPowerofTwo(self,n):
#     if n==0:
#         return False
#     if n&(n-1)==0:
#         return True
#     else:
#         return False

'''
# approach 4:
'''
def isPowerofTwo(n):
    i=0
    N=0
    while N<=n:
        N=2**i
        if N ==n:
            return True
        i=i+1
    return False
'''
print(isPowerofTwo(N))
