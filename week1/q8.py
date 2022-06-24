


# 1, 0
# 2, 0, 1
# 3 , 0,1, 2

def Fibonacci(limit):
    first = 0
    second = 1
    if (limit == 0):
        print(first)
    elif (limit == 1):
        print(second)
    else:
        total = first + second
        updatedPrev = second
        prev = second
        print(first)
        print(second)
        while (limit > 2):
            updatedPrev = total
            print(total)
            total += prev
            prev = updatedPrev
            limit -= 1






limit = int(input("Enter the limit: "))
Fibonacci(limit)


