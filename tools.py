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