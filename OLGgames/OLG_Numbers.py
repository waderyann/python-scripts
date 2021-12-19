import random

numberList = []



def getNumber():
    return random.randrange(1,4)

def listInsert(numberToAdd):
    numberList.append(validateNumber(numberList, numberToAdd)) 
    return numberList

def listLength():
    return len(numberList)

#Makes sure that a number isnt repeated within the list
def validateNumber(numberLists, numberToAdd):
    if numberToAdd in numberList:
        numberToAdd = getNumber()
        print("check")
        validateNumber(numberList, numberToAdd)
    return numberToAdd

for i in range(3):
    print(listInsert(getNumber()))

#print(numberList)