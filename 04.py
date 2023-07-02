givenNumber = int(input("Enter The Number:"))
fact = 1
for i in range(givenNumber, 0, -1):
    fact = fact*i
print(f"Factorial is {fact}")
