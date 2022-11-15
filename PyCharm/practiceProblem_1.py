# -----------------------------------Your age in 2090-------------------------------------$
num = input("pls enter your year of birth or you can enter your age:\n")

try:

    #year of birth when entered
    if len(num) == 4 and int(num) % 1 == 0:
        print(f"your current age is {2022 - int(num)}")

        if int(num) > 2022:
            print("you are not borned yet!")
        elif 2022 - int(num) >= 150:
            print(f"you seem to be oldest person alive!")
        else:
            print("entered year of birth is", num)
            hundred = int(num) + 100
            print("You will turn 100 in the year", hundred)
            interestedYear = int(input('enter the year you wanna know your age in:\n'))
            print(f"your age in the year {interestedYear} will be {interestedYear - int(num)}")


    #when age is entered
    elif int(num) % 1 == 0:
        print("entered age is", num)
        YOB = 2022 - int(num)
        hundred = YOB + 100
        print("You will turn 100 in the year", hundred)
        interestedYear = int(input('enter the year you wanna know your age in:\n'))
        print(f"your age in the year {interestedYear} will be {interestedYear - YOB}")

except Exception:
    print("Invalid input. Pl enter valid YOB or age.")
