# In welke subgrid zit de huidige plek

def get_subgrid(row,column):
    if row == 0 or row == 1 or row == 2:
        if column == 0 or column == 1 or column == 2:
            return 0
        if column == 3 or column == 4 or column == 5:
            return 1
        if column == 6 or column == 7 or column == 8:
            return 2

    if row == 3 or row == 4 or row == 5:
        if column == 0 or column == 1 or column == 2:
            return 3
        if column == 3 or column == 4 or column == 5:
            return 4
        if column == 6 or column == 7 or column == 8:
            return 5

    if row == 6 or row == 7 or row == 8:
        if column == 0 or column == 1 or column == 2:
            return 6
        if column == 3 or column == 4 or column == 5:
            return 7
        if column == 6 or column == 7 or column == 8:
            return 8


def matrix_to_subgrids(matrix):
    subgrids = [[],
                [],
                [],
                [],
                [],
                [],
                [],
                [],
                []]
    subgrids[0] = [list(matrix[0][0:3]), list(matrix[1][0:3]), list(matrix[2][0:3])]
    subgrids[1] = [list(matrix[0][3:6]), list(matrix[1][3:6]), list(matrix[2][3:6])]
    subgrids[2] = [list(matrix[0][6:9]), list(matrix[1][6:9]), list(matrix[2][6:9])]

    subgrids[3] = [list(matrix[3][0:3]), list(matrix[4][0:3]), list(matrix[5][0:3])]
    subgrids[4] = [list(matrix[3][3:6]), list(matrix[4][3:6]), list(matrix[5][3:6])]
    subgrids[5] = [list(matrix[3][6:9]), list(matrix[4][6:9]), list(matrix[5][6:9])]

    subgrids[6] = [list(matrix[6][0:3]), list(matrix[7][0:3]), list(matrix[8][0:3])]
    subgrids[7] = [list(matrix[6][3:6]), list(matrix[7][3:6]), list(matrix[8][3:6])]
    subgrids[8] = [list(matrix[6][6:9]), list(matrix[7][6:9]), list(matrix[8][6:9])]

    return subgrids
