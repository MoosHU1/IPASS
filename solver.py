
loop = 0
def solve(matrix):
    global loop
    find = find_empty(matrix)
    if not find:
        return True
    else:
        row, col = find

    #Niet oplosbaar
    if loop > 100000:
        return 0


    for i in range(1, 10):
        if valid(matrix, i, (row, col)):
            matrix[row][col] = i

            if solve(matrix):
                return True

            matrix[row][col] = 0

    loop += 1
    return False


#Checkt of het getal ingevuld kan worden volgens de regels van sudoku
def valid(matrix, num, pos):
    # Check row
    for i in range(len(matrix[0])):
        if matrix[pos[0]][i] == num and pos[1] != i:
            return False

    # Check column
    for i in range(len(matrix)):
        if matrix[i][pos[1]] == num and pos[0] != i:
            return False

    # Check matrixx
    matrixx_x = pos[1] // 3
    matrixx_y = pos[0] // 3

    for i in range(matrixx_y*3, matrixx_y*3 + 3):
        for j in range(matrixx_x * 3, matrixx_x*3 + 3):
            if matrix[i][j] == num and (i,j) != pos:
                return False

    return True


#Vindt de volgende lege cel die ingevuld moet worden
def find_empty(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                return (i, j)  # row, col

    return None