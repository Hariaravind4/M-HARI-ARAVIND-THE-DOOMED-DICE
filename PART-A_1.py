#using for loop
def printTotalCombinations(n):
    sum=0
    for i in range(n):
        for j in range(n):
            sum+=1
    print(sum)
noOfFace=6
print("The total possible combinations using for loop is",end=" ")
printTotalCombinations(noOfFace)


#using formula
noOfFaces=6 
totalCombinations=noOfFaces*noOfFaces
print("The total possible combinations using formula is",totalCombinations)

