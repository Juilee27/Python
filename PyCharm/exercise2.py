#exercise 2 - faulty calculator
# design a calculator which will solve all problems correctly except the following ones:
# # 45*3 = 555 , 56+9 = 78, 56/6= 6
# your program should take operator and the 2 numbers as input from the user and the return the result
while 1:
                                a = int(input('enter first no: '))
                                op = input('enter desired operator out of + - * / : ')
                                b = int(input('enter second no: '))

                                if a == 45 and b== 3 and op == '*':
                                    print('result = 555')
                                elif a == 56 and b == 9 and op == '+':
                                    print('result = 78')
                                elif a== 56 and b == 6 and op == '/' :
                                    print('result = 6')
                                elif op == "+":
                                    print('result = ', a+b)
                                elif op == "-":
                                    print('result =', a-b)
                                elif op == "*":
                                    print('result = ', a*b)
                                elif op == "/":
                                    print('result =', a/b)


