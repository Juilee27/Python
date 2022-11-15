l1 = ['bhindi', 'aloo', 'tomato', 'butter']

# i=1
# for item in l1:
#     if i%2 is not 0:
#         print(f'jarvis plz buy {item}')
#     i+=1

##note - ABOVE CODE CAN BE MADE SIMPLE WITH ENUMERATE FUNCTION------##

for index,item in enumerate(l1):
    if index %2 ==0:
        print(f'jarvis plz buy {item}')
