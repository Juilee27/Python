# time module

#we are trying to calculate time taken by for loop and while loop
import time
#
initial = time.time()
# print(initial)
#
k=0
while k<45:
    print('this is jui')
    k+=1
    time.sleep(2.5) #to delay execution by 2.5 sec
print('while loop ran in time: ', time.time()- initial, 'seconds')
#
# initial2 =time.time()
# for i in range (45):
#     print('helloz')
# print('for loop ran in time: ', time.time()- initial2, 'seconds')


# localtime = time.asctime(time.localtime(time.time()))
# print(localtime)
