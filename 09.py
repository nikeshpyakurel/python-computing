givenString = input("Enter The String:")
reversedString = ''
counter = 0
while counter < len(givenString):
    reversedString = givenString[counter]+reversedString
    counter = counter+1
print(reversedString)
