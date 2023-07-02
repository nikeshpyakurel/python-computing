givenString = input("Enter The String:")
reversedString = ''
counter = 0
lengthOfString = givenString.__len__()-1
decreace = lengthOfString
while counter <= lengthOfString:
    reversedString = reversedString[counter]+givenString[decreace]
    counter = counter+1
    decreace = decreace-1

print(reversedString)
