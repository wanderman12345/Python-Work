
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
out = []
test_dict = {}
for i in a:
    test_dict[i] = "true"

for j in b:
    if test_dict.get(j) == "true":
        out.append(j)

print(out)







