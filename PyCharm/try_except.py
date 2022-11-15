n1 = input('enter num 1: ')
n2 = input('enter num 2: ')
#try except is used in case of internet connectivity applications for eg, if someone wants to donwload
# something and there is net connectivity issue, in this case program must not exit due to error,
# it shld give user direction to what solution can be used

try:
    print('sum is: ',
        int(n1)+ int(n2))
except Exception as e:
        print(e)

print('this is very important')