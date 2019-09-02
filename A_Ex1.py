R = int(input("Enter the number of rows:")) 
C = int(input("Enter the number of columns:")) 

# Initialize matrix 
matrix = [] 
print("Enter the entries rowwise:") 

# For user input 
for i in range(R):		 # A for loop for row entries 
	a =[] 
	for j in range(C):	 # A for loop for column entries 
		a.append(int(input())) 
	matrix.append(a) 

# For printing the matrix 
for i in range(R): 
	for j in range(C): 
		print(matrix[i][j], end = " ") 
	print()

def find_min(line):
    return min(line)

def check_sides(matrix, x, y):
    new_matrix = matrix[y-1:y+2]# Take the previous, current and next lines and columns.
    
    
    for line in new_matrix:
        if matrix[y][x] > min(line[x-1:x+2]): 
            return False

    return True

def find_local_minima(matrix):
    local_minimas = []

    for y, line in enumerate(matrix):

        if y == 0 or y == len(matrix) - 1: continue # Skip first and last lines

        for x, element in enumerate(line):
            if x == 0 or x == len(line) - 1: continue # Skip first and last columns

            if check_sides(matrix, x, y): # Test the 8 surrounding numbers 
                local_minimas.append((x, y)) # Set the location of the number if it passes
    
    return local_minimas

print(len(find_local_minima(matrix)))



