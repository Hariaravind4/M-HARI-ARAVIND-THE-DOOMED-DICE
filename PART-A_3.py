  #total no of combinations
def printProbabilty(n):
    dice=[[0]*n for _ in range(n)] 
    for i in range(1,n+1):
        for j in range(1,n+1):
            dice[i-1][j-1]=i+j      
    probabilty= {}
    for i in range(2, (n*2)+1):  
        favourableOccurences= sum(row.count(i) for row in dice) 
        probabilty[i] = favourableOccurences/ totalCombinations
    for k, v in probabilty.items():
        print("P(Sum='{}'): {:.3f}".format(k, v))  

noOfFaces=6
totalCombinations=6*6
print("Probability of all possible sums:")
printProbabilty(noOfFaces)