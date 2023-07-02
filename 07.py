takeString = input("Enter Ther String:")
countDigit = 0
countLetter = 0
countSpace = 0
for i in takeString:
    if i.isspace() == True:
        countSpace = countSpace+1

print(f"The Total Count of Space is :{countSpace}")
