from solver import *
import random
from tools import *
import numpy

def find_next(dict, dif):
    #Lijst met keys die kunnen worden gedugt
    dugable = []
    for key, value in dict.items():
        if value == 1:
            dugable.append(key)

    if len(dugable) == 0:
        return None

    else:
        #Voor elke moeilijkheidsgraad is er een verschillend dug patroon
        if dif == "easy":
            return random.choice(dugable)
        elif dif == "medium":
            return dugable[0]





def check_valid(matrix, row, column, dif):
    correct_num = matrix[row,column]

    nums = [1,2,3,4,5,6,7,8,9]
    nums.remove(correct_num)

    subgrid = get_subgrid(row,column)
    subgrids = matrix_to_subgrids(matrix)

    #Eerst moet er gekeken worden of als je deze cel dugt je een restrictie verbreekt (operation 2)

    if dif == "easy":
        randomized_bound = random.randrange(36,50)
        if numpy.count_nonzero(matrix==0) > randomized_bound:
            return False
        elif numpy.count_nonzero(matrix[row]==0) >=4  or numpy.count_nonzero(matrix[:,column]==0) >=4:
            return False

    for num in nums:
        #Het getal wat je gaat testen moet natuurlijk wel aan de regels voldoen
        if num not in matrix[row] and num not in matrix[:, column] and num not in subgrids[subgrid][0] \
                and num not in subgrids[subgrid][1] and num not in subgrids[subgrid][2]:

            temp_matrix = matrix
            temp_matrix[row,column] = num

            #Als er geen oplossing is ga dan verder
            if solve(temp_matrix) == 0:
                continue
            else:
                return False


    return True

def dig(matrix, dif):
    dict = {}
    print("AAAAAAAAAAAAAAA")
    # 1 betekent "can be dug", 0 betekent "can't be dug"
    for i in range(0, 9):
        for j in range(0, 9):
            dict.update({(i, j): 1})

    while 1==1:
        print(matrix)
        next = find_next(dict, dif)


        if next != None:
            if find_next(dict, dif) == None:
                return matrix
            else:
                # Is er voor alle getallen geen oplossing dan kan de cel worden gedugt
                if check_valid(matrix, next[0], next[1], dif) == True:
                    matrix[next[0], next[1]] = 0
                    dict[next[0],next[1]] = 0
                else:
                    dict[next] = 0
        #Als er geen cellen meer gedugt kunnen worden is de sudoku klaar
        else:
            return matrix

        







