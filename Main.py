'''Bron 1 create_grid: https://www.daniweb.com/programming/software-development/threads/446765/making-multiple-entry-matrixxes-in-a-for-loop'''


import tkinter as tk
import random as random
import numpy
from solver import *
from dig_holes import *
from tools import *

master = tk.Tk()
master.geometry("600x400")



def create_button():
    b = tk.Button(master, text="OK")
    b.grid()


def generate_solved():
    # matrix1 = [
    #     [0, 0, 0, 0, 0, 0, 0, 0, 0]
    #     [0, 0, 0, 0, 0, 0, 0, 0, 0]
    #     [0, 0, 0, 0, 0, 0, 0, 0, 0]
    #     [0, 0, 0, 0, 0, 0, 0, 0, 0]
    #     [0, 0, 0, 0, 0, 0, 0, 0, 0]
    #     [0, 0, 0, 0, 0, 0, 0, 0, 0]
    #     [0, 0, 0, 0, 0, 0, 0, 0, 0]
    #     [0, 0, 0, 0, 0, 0, 0, 0, 0]
    #     [0, 0, 0, 0, 0, 0, 0, 0, 0]
    # ]

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
        column = 0
        while column < 9:
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
                    print(subgrids)
                    print(matrix)
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
            print("\n\n")

        row+=1
    return matrix



def draw_grid(matrix_get):
    master.title('Grid')
    entries = []

    b = 0
    for ncolumn in range(1, 10):
        for nrow in range(1, 10):
            # create entries list
            if (ncolumn == 4 or ncolumn == 5 or ncolumn == 6) and (nrow == 1 or nrow == 2 or nrow == 3):
                entries.append(tk.Entry(master, width=5, background='grey'))
            elif (ncolumn == 1 or ncolumn == 2 or ncolumn == 3 or ncolumn == 7 or ncolumn == 8 or ncolumn == 9) and (
                    nrow == 4 or nrow == 5 or nrow == 6):
                entries.append(tk.Entry(master, width=5, background='grey'))
            elif (ncolumn == 4 or ncolumn == 5 or ncolumn == 6) and (nrow == 7 or nrow == 8 or nrow == 9):
                entries.append(tk.Entry(master, width=5, background='grey'))
            else:
                entries.append(tk.Entry(master, width=5))

            # grid layout the entries
            entries[b].grid(row=nrow, column=ncolumn)
            # bind the entries return key pressed to an action
            # master.entries[n].bind('<Return>', partial(master.action, n))
            b += 1


    matrix = []
    for column in range(9):
        for row in range(9):
            matrix.append(matrix_get[row][column])


    for i in range (0,81):
        entries[i].insert('end', matrix[i] )




#
# create_button()
# draw_grid(generate_solved())
# master.mainloop()
matrix = [
    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7]
]
# matrix = [
#     [1, 2, 3, 4, 5, 6, 7, 8, 9],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 2, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 1, 3, 4],
#     [2, 0, 0, 0, 0, 0, 5, 6, 0],
#     [0, 0, 0, 0, 0, 0, 7, 8, 9]
# ]

draw_grid(dig(generate_solved(), "medium"))
master.mainloop()
