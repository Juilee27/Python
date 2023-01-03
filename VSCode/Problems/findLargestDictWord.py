# Find largest word in dictionary
d = ["ale", "apple", "monkey", "plea"] #str1[i] m  ["a", "b", "c"]#
S = "abpcplea" #str2[j] n

def findLongestWord(S,d):
        res =''        
        # list(d).sort()
        for m in sorted(d):
            i=0
            j=0
            while i<len(m) and j<len(S):
                if m[i] == S[j]:
                    i+=1
                    j+=1
                else:
                    j+=1
            if i==len(m) and len(res) < len(m):
                res= m
            # isSubsequence(m, S
        print(res)

findLongestWord(S,d)

'''
Steps:
Basically finding if a string is subset of another string sequence. 
1. sort given dictionary.
2. Take a dict element(it is string). Iterate over both strings.
3. Check if string is present in given sequence. If yes, save element to var res.
4. To check for longest element, check if len of current element is greater than that of previous.
5. Run above steps for all elements of the dictionary.  
'''



