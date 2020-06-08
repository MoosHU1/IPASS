'''Bron 1 create_grid: https://www.daniweb.com/programming/software-development/threads/446765/making-multiple-entry-boxes-in-a-for-loop'''


import tkinter as tk
import random as random
import numpy

master = tk.Tk()
master.geometry("600x400")

# def create_grid():
#         master.title('Grid')
#         entries = []
#
#         b = 0
#         for ncolumn in range(1,10):
#             for nrow in range(1,10):
#                 # create entries list
#                 if (ncolumn == 4 or ncolumn == 5 or ncolumn == 6) and (nrow == 1 or nrow == 2 or nrow == 3):
#                     entries.append(tk.Entry(master, width=5, background='grey'))
#                 elif (ncolumn == 1 or ncolumn == 2 or ncolumn == 3 or ncolumn == 7 or ncolumn == 8 or ncolumn == 9) and (nrow == 4 or nrow == 5 or nrow == 6):
#                     entries.append(tk.Entry(master, width=5, background='grey'))
#                 elif (ncolumn == 4 or ncolumn == 5 or ncolumn == 6) and (nrow == 7 or nrow == 8 or nrow == 9):
#                     entries.append(tk.Entry(master, width=5, background = 'grey'))
#                 else:
#                     entries.append(tk.Entry(master, width=5))
#
#                 # grid layout the entries
#                 entries[b].grid(row=nrow, column=ncolumn)
#                 # bind the entries return key pressed to an action
#                 #master.entries[n].bind('<Return>', partial(master.action, n))
#                 b+=1
#
#
#         entries[1].insert('end', 4)

    # def action(master, ix, event):
    #     '''this entry return key pressed'''
    #     text = master.entries[ix].get()
    #     info = "entry ix=%d text=%s" % (ix, text)
    #     # use first entry to show test results
    #     # clear old text
    #     master.entries[0].delete(0, 'end')
    #     # insert new text
    #     master.entries[0].insert('end', info)



def create_button():
    b = tk.Button(master, text="OK")
    b.grid()


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


def backtracking():
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
    #TODO while loop maken die als de rij niet klopt opnieuw gaat beginnen tot dat hij een kloppende rij heeft
    row = 0
    column = 0
    while row<9:
        column = 0
        while column < 9:

            #In welke subgrid zit de huidige plek
            if row == 0 or row == 1 or row == 2:
                if column == 0 or column == 1 or column == 2:
                    subgrid = 0
                if column == 3 or column == 4 or column == 5:
                    subgrid = 1
                if column == 6 or column == 7 or column == 8:
                    subgrid = 2

            if row == 3 or row == 4 or row == 5:
                if column == 0 or column == 1 or column == 2:
                    subgrid = 3
                if column == 3 or column == 4 or column == 5:
                    subgrid = 4
                if column == 6 or column == 7 or column == 8:
                    subgrid = 5

            if row == 6 or row == 7 or row == 8:
                if column == 0 or column == 1 or column == 2:
                    subgrid = 6
                if column == 3 or column == 4 or column == 5:
                    subgrid = 7
                if column == 6 or column == 7 or column == 8:
                    subgrid = 8


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

def draw_grid():
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


    matrix_get = backtracking()
    matrix = []
    for column in range(9):
        for row in range(9):
            matrix.append(matrix_get[row][column])


    for i in range (0,81):
        entries[i].insert('end', matrix[i] )




create_button()
draw_grid()
master.mainloop()

