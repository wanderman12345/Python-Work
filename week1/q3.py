

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
number = int(input("Enter a limiting number: "))

max = number
out = []
for i in a:
    if i < max:
        out.append(i)
print(out)
