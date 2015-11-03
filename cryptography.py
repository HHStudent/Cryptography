"""
cryptography.py
Author: <your name here>
Credit: <list sources used, if any>

Assignment:

Write and submit a program that encrypts and decrypts user data.

See the detailed requirements at https://github.com/HHS-IntroProgramming/Cryptography/blob/master/README.md
"""
associations = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 .,:;'\"/\\<>(){}[]-=_+?!"
command = str(input("Enter e to encrypt, d to decrypt, or q to quit: "))

def encrypt():
    list1 = []
    list2 = []
    for x in message:
        letter = associations.find(x)
        list1.append(letter)
    for y in key:
        keyletter = associations.find(x)
        list2.append(keyletter)
    list3 = [x + y for x, y in zip(list1, list2)]
    list4 = []
    for n in list3:
        l = associations[n]
        list4.append(l)
    print(list4)




if command == "e":
    message = str(input("Message: "))
    key = str(input("Key: "))
    encrypt()
elif command == "d":
    dmessage = str(input("Message: "))
    dkey = str(input("Key: "))
elif command == "q":
    print("Goodbye!")
else:
    print("Did not understand command, try again.")

