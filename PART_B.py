def calculateProbability(A,B):
    occurrences=[0]*11
    for i in range(len(A)):
        for j in range(len(B)):
            possibleSum=A[i]+B[j]
            occurrences[possibleSum-2]+=1
    return occurrences
def findDieA(A):
    for i in range(len(A)):
        if A[i]>4:
            A[i]-=3

def calculateCombinations(endValue,totalLength,startValue,dieB,A):
    if len(dieB) == totalLength:
        dieB1=list(dieB)
        if calculateProbability(A,dieB1)==initialProbability:
            dieB1.sort()
            print("Undoomed Dice B:",dieB1)
        return
    for i in range(startValue,endValue+ 1):
        dieB.append(i)
        calculateCombinations(endValue,totalLength,i+1,dieB,A)
        dieB.pop()

def undoomDice(A,B):
    findDieA(A)
    A.sort()
    print("Undoomed Dice A:",A)
    dieB=[]
    temp=8
    dieB.append(1)
    dieB.append(temp)
    calculateCombinations(temp-1,6,2,dieB,A)

A=[1, 2, 3, 4, 5, 6]
B=[1, 2, 3, 4, 5, 6]
print("Intial Dice A:",A)
print("Intial Dice B:",B)
initialProbability=[0]*11
initialProbability=calculateProbability(A,B)
undoomDice(A,B)


