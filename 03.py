takeString = input("Enter Ther String:")
countDigit = 0
countLetter = 0
countSpace = 0
for i in takeString:
    if i.isdigit() == True:
        countDigit = countDigit+1
    elif i.isalpha() == True:
        countLetter = countLetter+1
    elif i.isspace() == True:
        countSpace = countSpace+1
print(f"The Total Count of Digit is :{countDigit}")
print(f"The Total Count of Letter is :{countLetter}")
print(f"The Total Count of Space is :{countSpace}")
