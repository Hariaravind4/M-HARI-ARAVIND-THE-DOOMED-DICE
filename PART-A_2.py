#To find the distribution of all possible combination
def printTotalDistribution(n):
    dice=[]
    for i in range(1,n+1):  
        for j in range(1,n+1):
            dice=[] 
            dice.append(i)
            dice.append(j)
            print(dice,end="=")
            print(i+j,end=" ")
        print() 
noOfFace=6
print("The distribution of all possible combination:")
printTotalDistribution(noOfFace)





