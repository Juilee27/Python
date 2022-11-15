f1 = open('harry.txt')

try:
    f= open('does.txt')

#we can write multiple except statements

except Exception as e:
    print(e)

except EOFError as e:
    print('EOF error aya he')

except IOError as e:
    print(e)

else: #this will run only when Exception is not running and vice versa
    print('this will run only when Exception is not running')

finally: #finally is used for code cleanup generally
    #finally runs anyway irrespective of anything
    print('run this anyway...')
    # f.close()
    f1.close()

print('important stuff')