import random

numberList = []



def getNumber():
    return random.randint(1,49)

def getNumber_50():
    return random.randint(1,50)

def listInsert(numberToAdd):
    numberList.append(validateNumber(numberList, numberToAdd)) 
    return numberList

def listLength():
    return len(numberList)

#Makes sure that a number isnt repeated within the list
def validateNumber(numberList, numberToAdd):
    if numberToAdd not in numberList:
        return numberToAdd
    numberToAdd = getNumber()
    return validateNumber(numberList, numberToAdd)

def getOLGSet():
    for i in range(6):
     listInsert(getNumber())
    
def getOLGLottoMax():
    for i in range(7):
        listInsert(getNumber_50())

getOLGLottoMax()
numberList.sort()
print(numberList)
print("Good Luck!!")

#combination play 5/7/8/9

#print(numberList)
