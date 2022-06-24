
# palindrome
# ex: racecar (7)
# ex: hiih
#

word = input("Enter word to check palindrome: ")
slice = int(len(word)/2)
front = word[0:slice]


if len(word) % 2 == 0:
    back = word[slice:]

else:

    back = word[slice+1:]

back = back[::-1]

if (front == back):
    print("This is a palindrome")
else:
    print("This is not a palindrome")







