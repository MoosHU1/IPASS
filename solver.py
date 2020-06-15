from tools import *

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

    # Check submatrixx
    subgrids = matrix_to_subgrids(matrix)
    subgrid = get_subgrid(pos[0], pos[1])
    if num not in subgrids[subgrid][0] and num not in subgrids[subgrid][1] and num not in subgrids[subgrid][2]:
        return True
    else:
        return False



#Vindt de volgende lege cel die ingevuld moet worden
def find_empty(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                return (i, j)  # row, col

    return None