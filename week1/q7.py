#to find an armstrong number

number = int(input("Enter the number: "))

#get number of digits

tempnumber = number
numDigits = 0
while tempnumber > 0:
    numDigits += 1
    tempnumber = int(tempnumber/10)

#calculate narcissistic number
tempnumber = number
total = 0
while tempnumber > 0:
    temp = tempnumber % 10
    tempnumber = int(tempnumber/10)
    total += temp**numDigits


print(total)