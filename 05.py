givenNumber = int(input("Enter a number: "))
sum = 0
temp = givenNumber

num_digits = len(str(givenNumber))

while temp > 0:
    digit = temp % 10
    sum += digit ** num_digits
    temp //= 10

if givenNumber == sum:
    print(givenNumber, "is an Armstrong number")
else:
    print(givenNumber, "is not an Armstrong number")
