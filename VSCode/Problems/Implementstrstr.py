'''
Problem: Implement strstr
https://practice.geeksforgeeks.org/problems/implement-strstr/1?page=1&difficulty[]=-1&sortBy=submissions

Approach:
1. check if x in s. 
2. if yes, iterate over s. Pick group in s of len(x) from index of s. If matches x, return that 1st index of s. 
Otherwise, jump to next index of s, pick group of len(x) and check same.
3. else return -1.
'''

s = 'ababaaaaaa'  
x = 'abaa'

def strstr(s, x):
    i = 0
    #check if x in s
    if x in s:
        #iterate over s
        while i < len(s):
            m = ''
            # Pick group in s of len(x) from index i of s.
            for j in range(i, i+len(x)):
                m += s[j]  #populate m
            # check if string m matches x
            if m == x:
                #if matches return index of s
                return i
            # else jump to next index of s
            i += 1
    #else return -1
    return -1

print(strstr(s, x))