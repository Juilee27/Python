import sklearn


def printhar(string):
    return f'ye string harry ko de de thakur {string}'


def add(num1, num2):
    return num1 + num2 + 5


print("aand the name is", __name__)
if __name__ == '__main__':  ##NOTE = NAME==MAIN WHEN WE ARE RUNNING THE PROGRAM INSIDE SAME PROGRAM
    print(printhar('hahahah'))
    o = add(1, 7)
    print(o)
