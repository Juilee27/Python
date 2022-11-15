def print2(str1):
    print2(str1)  # this is recursion
    print('this is ' + str1)


# print('harry')

def factorial_iterative(n):
    """
    :param n: int
    :return: n * n-1 * n-2 * n-3 ....1
    """
    fac = 1
    for i in range(n):  # this starts i from 0 to n-1
        fac = fac * (i + 1)
    return fac

def factorial_recursive(n):
    """
    :param n: int
    :return: n * n-1 * n-2 * n-3 ....1
    """
    if n==1 or n ==0:
        return  1
    else:
        return n * factorial_recursive(n-1)

def fibonacci(n):
    """
    it calculates below series = adds previous 2 nos to give next number
     0 1 1 2 3 5 8 13 21 34.....
    """
    if n==1:
        return  0
    elif n==2:
        return 1
    else:
        return  fibonacci(n-1) + fibonacci(n-2)

num = int(input("enter no : "))
# print('factorial using iterative method: ',  factorial_iterative(num))
# print('factorial using iterative method: ',  factorial_recursive(num))
print('fibonacci using recursive method: ',  fibonacci(num))

#note - use recursion for simple programs , for bigger code it is difficult to debug n backtrack
# hence try to use iterative method as they are simpler and easy to backtrack and debug

# n!= n * n-1 * n-2 * n-3 ....1
# n! = n * (n-1)!
