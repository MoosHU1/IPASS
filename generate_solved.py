import numpy
from tools import *
import random

def generate_solved():


    matrix = numpy.zeros(shape=(9, 9))
    subgrids = [

        [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ],
        [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ],
        [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ],
        [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ],
        [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ],
        [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ],
        [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ],
        [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ],
        [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ]



    ]

    #Gaat op elke plek een getal invullen
    row = 0
    column = 0
    while row<9:
        loop =0
        column = 0
        while column < 9:
            loop += 1
            subgrid = get_subgrid(row,column)

            correct = False
            nums= [1,2,3,4,5,6,7,8,9]
            while not correct:

                temp_num = random.choice(nums)

                #Check of het getal op de huidige plek aan de regels voldoet, zo ja vul hem dan in


                if temp_num not in matrix[row] and temp_num not in matrix[:,column] and temp_num not in subgrids[subgrid][0]\
                    and temp_num not in subgrids[subgrid][1] and temp_num not in subgrids[subgrid][2] :

                    matrix[row,column] = temp_num

                    if row == 0 or row == 3 or row == 6:
                        if column == 0 or column == 3 or column == 6:
                            subgrids[subgrid][0][0] = temp_num
                        if column == 1 or column == 4 or column == 7:
                            subgrids[subgrid][0][1] = temp_num
                        if column == 2 or column == 5 or column == 8:
                            subgrids[subgrid][0][2] = temp_num

                    if row == 1 or row == 4 or row == 7:
                        if column == 0 or column == 3 or column == 6:
                            subgrids[subgrid][1][0] = temp_num
                        if column == 1 or column == 4 or column == 7:
                            subgrids[subgrid][1][1] = temp_num
                        if column == 2 or column == 5 or column == 8:
                            subgrids[subgrid][1][2] = temp_num

                    if row == 2 or row == 5 or row == 8:
                        if column == 0 or column == 3 or column == 6:
                            subgrids[subgrid][2][0] = temp_num
                        if column == 1 or column == 4 or column == 7:
                            subgrids[subgrid][2][1] = temp_num
                        if column == 2 or column == 5 or column == 8:
                            subgrids[subgrid][2][2] = temp_num
                    column += 1

                    #print(matrix)
                    correct = True

                #Als deze rij niet meer correct ingevuld kan worden begin dan opnieuw met de rij
                #Daarvoor moet die rij ook in de matrix en subgrids gereset worden
                else:
                    try:
                        nums.remove(temp_num)
                    except:
                        matrix[row] = numpy.zeros(shape=(9))
                        subgrids = matrix_to_subgrids(matrix)
                        column = 0
                        correct=True

                    if len(nums) == 0:
                        matrix[row] = numpy.zeros(shape=(9))
                        subgrids = matrix_to_subgrids(matrix)
                        column = 0
                        correct=True
            #Als het te lang duurt om een oplossing voor de huidige kolom te vinden begin dan helemaal opnieuw
            if loop >500:

                loop=0
                matrix = numpy.zeros(shape=(9,9))
                subgrids = matrix_to_subgrids(matrix)
                column = 0
                row =0

        row+=1
    return matrix

