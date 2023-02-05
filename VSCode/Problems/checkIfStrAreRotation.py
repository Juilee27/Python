'''
Problem: Check if strings are rotations of each other or not.

https://practice.geeksforgeeks.org/problems/check-if-strings-are-rotations-of-each-other-or-not-1587115620/1?page=3&difficulty[]=-1&sortBy=submissions

approach:
1. take s2[0:3]. check if it is in s1. If yes, replace rest s1 with ''.
2. make part1 str that is reversed part of s2, part that is from s1.
3. check if rest part of s1 present in s2[0:]. 
'''
s1 = 'geeksforgeeks'
s2 = 'forgeeksgeeks'

#I delivered following code as per the above approach:
# def  areRotations(s1,s2):
#         #code here
#         # l = len(s2)
        # if len(s1) == len(s2):        
    #         i = s1.find(s2[0:3]) #this random 3 in range is not optimal solution.
    #         new_s1 = s1.replace(s1[i:len(s1)], '')
    #         part1 = s2[-1: -(len(new_s1)+1):-1][::-1]
    #         if new_s1 == part1:
    #                 if s1[i:] in s2[0:]:
    #                         return True
#         return False
# print(areRotations(s1,s2))


#OPTIMAL solutions are:
#Solution 1:
# def areRotations(s1,s2):
#         p=""
#         i=0

#         if len(s1)!= len(s2):
#             return False
           
#         while p!=s2:
#             #rotating s1 and saving to p
#             p=s1[i:]+s1[:i]
#             # print(id(p))
#             #whole s1 is rotated, still p!=s2
#             if i==len(s1):
#                 return 0
#             i+=1
#         #when p==s2
#         return 1
# print(areRotations(s1,s2))
#above same code with for loop: 
# for i in range(len(s1)):
#             if s1[i:]+s1[0:i] == s2:
#                 return True

#Solution 2: folllwing is best out the box solution!
def areRotations(s1,s2):
    if len(s1)==len(s2):
        #take str twice s2 and check if s1 is present in it meaning s1 is rotated
        if s1 in 2*s2:
            print(1)
    else:
        print(0)
areRotations(s1,s2)

'''
Takeaway: str is immutable. But we can play around it as if we try to change given str, it will just save it to new location.
'''
            
                