"""
cryptography.py
Author: Dimitri
Credit: http://stackoverflow.com/questions/3391076/repeat-string-to-certain-length, http://stackoverflow.com/questions/14050824/add-sum-of-values-of-two-lists-into-new-list

Assignment:

Write and submit a program that encrypts and decrypts user data.

See the detailed requirements at https://github.com/HHS-IntroProgramming/Cryptography/blob/master/README.md
"""
associations = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 .,:;'\"/\\<>(){}[]-=_+?!"
command = str(input("Enter e to encrypt, d to decrypt, or q to quit: "))

def rep(s, m):
    a, b = divmod(m, len(s))
    return s * a + s[:b]

def encrypt():
    list1 = []
    list2 = []
    for x in message:
        letter = associations.find(x)
        list1.append(letter)
    for y in key:
        keyletter = associations.find(y)
        list2.append(keyletter)
        list21 = rep(list2, len(list1))
    list3 = [x + y for x, y in zip(list1, list21)]
    list4 = []
    for n in list3:
        l = associations[n]
        list4.append(l)
    for x in list4:
        print(x, end='')

def decrypt():
    dlist1 = []
    dlist2 = []
    for x in dmessage:
        dletter = associations.find(x)
        dlist1.append(dletter)
    for y in dkey:
        dkeyletter = associations.find(y)
        dlist2.append(dkeyletter)
        list22 = rep(dlist2, len(dlist1))
    dlist3 = [x - y for x, y in zip(dlist1, list22)]
    dlist4 = []
    for m in dlist3:
        dl = associations[m]
        dlist4.append(dl)
    for x in dlist4:
        print(x, end='')

running = 0
while running == 0:
    if command == "e":
        message = str(input("Message: "))
        key = str(input("Key: "))
        encrypt()
        print(\n)
    elif command == "d":
        dmessage = str(input("Message: "))
        dkey = str(input("Key: "))
        decrypt()
        print(\n)
    elif command == "q":
        print("Goodbye!")
        running += 1
    else:
        print("Did not understand command, try again.")
        print(\n)

"""
if command == "e":
    message = str(input("Message: "))
    key = str(input("Key: "))
    encrypt()
elif command == "d":
    dmessage = str(input("Message: "))
    dkey = str(input("Key: "))
    decrypt()
elif command == "q":
    print("Goodbye!")
else:
    print("Did not understand command, try again.")
"""