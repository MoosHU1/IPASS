from solver import *
import random
from tools import *
import numpy

def find_next(dict, dif):
    #Lijst met keys(coordinaten) die kunnen worden gedugt
    dugable = []
    for key, value in dict.items():
        if value == 1:
            dugable.append(key)

    if len(dugable) == 0:
        return None

    else:
        #Voor elke moeilijkheidsgraad is er een verschillend dug patroon

        if dif == "easy" or dif == "medium" or dif == "difficult":
            #Kies een random cel
            return random.choice(dugable)


def check_valid(matrix, row, column, dif):
    correct_num = matrix[row,column]
    nums = [1,2,3,4,5,6,7,8,9]
    nums.remove(correct_num)

    subgrid = get_subgrid(row,column)

    subgrids = matrix_to_subgrids(matrix)

    #Eerst moet er gekeken worden of als je deze cel dugt je een restrictie verbreekt (operation 2)

    if dif == "easy":
        min_empty = 31
        max_empty = 45
        min_givens_rowcol = 5

    elif dif == "medium":
        min_empty = 45
        max_empty = 49
        min_givens_rowcol = 6

    elif dif == "difficult":
        min_empty = 49
        max_empty = 53
        min_givens_rowcol = 7
        order = [[i for i in range(0, 9)], [i for i in range(17, 8, -1)], [i for i in range(18, 27)],[i for i in range(35, 26, -1)],
                 [i for i in range(36, 44)],[i for i in range(53, 44, -1)], [i for i in range(54,63)], [i for i in range(71,62, -1)],[i for i in range(72,81)]]

    randomized_bound = random.randrange(min_empty, max_empty)
    if numpy.count_nonzero(matrix==0) > randomized_bound:
        return False

    elif numpy.count_nonzero(matrix[row]==0)>=min_givens_rowcol  or numpy.count_nonzero(matrix[:,column]==0)>=min_givens_rowcol:
        return False



    for num in nums:
        #Het getal wat je gaat testen moet natuurlijk wel aan de regels voldoen
        if num not in matrix[row] and num not in matrix[:, column] and num not in subgrids[subgrid][0] \
                and num not in subgrids[subgrid][1] and num not in subgrids[subgrid][2]:

            temp_matrix = numpy.empty_like(matrix)
            temp_matrix[:] = matrix
            temp_matrix[row,column] = num

            #Als er geen oplossing is ga dan verder
            if solve(temp_matrix) == 0:
                continue
            else:
                return False


    return True

def dig(matrix, dif):
    dict = {}

    #Dictionary met voor elke positie of hij wel of niet gedugged mag worden
    # 1 betekent "can be dug", 0 betekent "can't be dug"
    for i in range(0, 9):
        for j in range(0, 9):
            dict.update({(i, j): 1})

    while 1==1:

        next = find_next(dict, dif)



        if find_next(dict, dif) == None:
            # Als er geen cellen meer gedugt kunnen worden is de sudoku klaar
            return matrix
        else:
            # Is er voor alle getallen geen oplossing dan kan de cel worden gedugt
            if check_valid(matrix, next[0], next[1], dif) == True:
                matrix[next[0], next[1]] = 0
                dict[next[0],next[1]] = 0
            else:
                dict[next] = 0


        







