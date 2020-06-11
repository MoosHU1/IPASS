from solver import *
import random

def find_next(dict):
    #Lijst met keys die kunnen worden gedugt
    dugable = []
    for key, value in dict.items():
        if value == 1:
            dugable.append(key)

    if len(dugable) == 0:
        return None
    else:
        return random.choice(dugable)


def check_valid(matrix, row, column):
    correct_num = matrix[row,column]


    nums = [1,2,3,4,5,6,7,8,9]
    nums.remove(correct_num)

    for num in nums:
        #TODO Het getal wat je invuldt in temp matrix moet wel aan de regels voldoen
        if num not in matrix[row] and num not in matrix[:, column] and num not in subgrids[subgrid][0] \
                and num not in subgrids[subgrid][1] and num not in subgrids[subgrid][2]:

            temp_matrix = matrix
            temp_matrix[row,column] = num

        #Als er geen oplossing is ga dan verder
        if solve(temp_matrix) == 0:
            continue
        else:
            print(solve(temp_matrix))
            return False


    return True

def easy(matrix):
    dict = {}
    print("AAAAAAAAAAAAAAA")
    # 1 betekent "can be dug", 0 betekent "can't be dug"
    for i in range(0, 9):
        for j in range(0, 9):
            dict.update({(i, j): 1})

    while 1==1:
        print(matrix)
        next = find_next(dict)

        if next != None:
            if find_next(dict) == None:
                return matrix
            else:
                # Is er voor alle getallen geen oplossing dan kan de cel worden gedugt
                if check_valid(matrix, next[0], next[1]) == True:
                    matrix[next[0], next[1]] = 0
                else:
                    dict[next] = 0

        else:
            return matrix

        







