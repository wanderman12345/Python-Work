

number = int(input("Enter a number: "))
check = int(input("Enter a number to check: "))

if number % check == 0:
    print("The number is divided perfectly by check")
else:
    if number % 2 == 0:
        if number % 4 == 0:
            print("The number is a multiple of 4")

        print("The number is even")
    else:
        print("The number is odd")

