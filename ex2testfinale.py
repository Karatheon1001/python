R = int(input("Enter the number of rows:")) 
C = int(input("Enter the number of columns:")) 

# Initialize matrix 
matrix = [] 
print("Enter the entries rowwise:") 

# For user input 
for i in range(R):         # A for loop for row entries 
    a =[] 
    for j in range(C):     # A for loop for column entries 
        a.append(int(input())) 
    matrix.append(a) 

# For printing the matrix 
for i in range(R): 
    for j in range(C): 
        print(matrix[i][j], end = " ") 
    print()

def adjzeroes(R):
    seq=0
    count=0
    for el in R:
        if el==1:
            count=0
        else:
            count+=1
            seq=max(seq,count)
            
    return seq
counter=0
l=[]
for R in matrix:
    counter=adjzeroes(R)
    l.append(counter)
print ("the longest sequence of zeroes is",max(l))
