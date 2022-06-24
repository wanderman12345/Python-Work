
name = input("Enter your name: ")
age = int(input("Enter your age: "))
loop = int(input("Enter number for loop: "))
currentYear = 2022
offsetYears = 100-age
predictedYear = currentYear + offsetYears

for i in range(0,loop):
    print("The year at which you will be 100 is {}".format((str(predictedYear))))


