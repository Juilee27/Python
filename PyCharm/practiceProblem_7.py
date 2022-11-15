# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Search Engine~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

''' #my solution where relevance order part is not working yet
def searchEngine(sentences, strim):
    # python is - user input
    match_count = 0
    counts = []

    print(f"3 results found:")

    for i in sentences:  # taking element in list Sentences
        if strim.lower() in i.lower(): #correct - doni lower case krun string search keli
            s = strim.lower().split() #list - str cha word ni word milayla split kela
            # e = i.lower().split() #list - not required, we searched in str directly instead of list
            for r in s: #taking every word in str
                match_count = i.lower().count(r) #correct - searching and counting every word in item string
                # print(r, match_count)

            # print(f"{i}")

if __name__ == '__main__':
    Sentences = ["Python is cool", "python is good", "python is not python", "snake"]
    str = input("Enter what u wanna search:\n")
    searchEngine(Sentences, str)
'''

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~below is harry's solution~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def searchEngine(sentence1, sentence2):
    sen1 = sentence1.split()  # list - query
    sen2 = sentence2.split()  # list - given list item
    match_count = 0
    for s1 in sen1:
        for s2 in sen2:
            if s1.lower() == s2.lower(): #list item and query doghana lower case krun
                match_count += 1

    return match_count


if __name__ == '__main__':
        Sentences = ["python is a good", "this is snake", "harry is a good boy", "Subscribe to code with harry"]
        query = input("Please input your query string\n")
        # for Sentence in Sentences:
        #     scores = [searchEngine(query, Sentence)]  #ithe mala match count milnar
        #list comprehension kerna!
        scores = [searchEngine(query, Sentence) for Sentence in Sentences]  # ithe mala match count milnar for all items in list
        # print(scores)
        sortedSentScores = [sentScore for sentScore in sorted(zip(scores, Sentences), reverse= True)]
        # print(sortedSentScores)
        print(f"{len(sortedSentScores)} results found:") #print results found
        for score, item in sortedSentScores:
            if score != 0:
                print(f'"{item}": with the score of {score}')
            else:
                print("No match found.")

