givenNumber = int(input("Enter Prime"))
notPrimeNo = False
if givenNumber == 1:
    print("Not prime")
elif givenNumber > 1:
    for i in range(2, givenNumber):
        if givenNumber % i == 0:
            notPrimeNo = True
            break

    if notPrimeNo:
        print('not prime')
    else:
        print('prime')
