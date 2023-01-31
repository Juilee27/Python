'''
Problem: Find first repeated character
https://practice.geeksforgeeks.org/problems/find-first-repeated-character4108/1?page=3&difficulty[]=-1&status[]=unsolved&sortBy=submissions

approach:
1. iterate over S. 
2. create empty hashmap. If character not present in hashmap, put it in hashmap. Else it means it is repeating. That is lowest repeated index. Return this char.
3. If no char repeating, return -1.

'''

S ="lptpgwgjrwlgtdhd"
def firstRepChar(s):
    hashmap = {}
    for i in range(len(s)):
        if s[i] in hashmap: #s[i] is repeating
            return s[i]
        else:
            hashmap[s[i]] = i #add s[i] in hashmap
    return -1

print(firstRepChar(S))                        

# approach 2:
#         i = len(s)-1
#         temp = -1
#         while i > 0:
#             if s[i] in s[:i]:
#                 temp = s[i]
#             i -= 1
#         return temp