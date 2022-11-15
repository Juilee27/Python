# -------------------------Divide the apples--------------------------------

try:
    n = int(input("enter number of apples:\n"))
    mn = int(input("enter minimum number of the range:\n"))
    mx = int(input("enter max number of the range:\n"))


except ValueError:
    print("Invalid input. Enter integers only.")
    # exit()

if mn == mx:
        print(f"as they are equal, this is not a range. Result is {n/mn}")
else:
    for i in range(mn, mx+1):
        if n%i == 0:
            print(f"{i} is divisor of {n}")
        elif n%i != 0:
            print(f"{i} is not a divisor of {n}")





