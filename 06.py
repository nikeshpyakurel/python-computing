givenNumber = int(input("Enter a number: "))

sum = 0
for i in range(1, givenNumber):
    if givenNumber % i == 0:
        sum += i

if sum == givenNumber:
    print(givenNumber, "is a perfect number")
else:
    print(givenNumber, "is not a perfect number")
