'''Bron 1 create_grid: https://www.daniweb.com/programming/software-development/threads/446765/making-multiple-entry-matrixxes-in-a-for-loop
Bron 2: https://stackoverflow.com/questions/6431973/how-to-copy-data-from-a-numpy-array-to-another
'''


import tkinter as tk
from Algorithmic.dig_holes import *
from Algorithmic.generate_solved import *

master = tk.Tk()
master.geometry("600x400")




def draw_grid(matrix_digged,matrix_answer):
    def create_button_check():
        # b = tk.Button(master, text="OK")
        # b.grid()


        entries_get = []
        for i in range(0, 81):
            if entries[i].get() != "":
                entries_get.append(int(entries[i].get()))
            else:
                entries_get.append(0)

        user_input = entries_to_matrix(entries_get)

        correct = True
        for row in range(0,9):
            for column in range(0,9):
                if user_input[row][column] != 0 and matrix_answer[row][column] != user_input[row][column]:
                    label.config(fg="red")
                    correct=False
                    var.set("")
                    var.set("Fout")

        if correct:
            if numpy.count_nonzero(user_input == 0) == 0:
                label.config(fg="green")
                var.set("")
                var.set("Gehaald!!")
            else:
                label.config(fg="green")
                var.set("")
                var.set("Goed")

    def create_button_new_easy():
        solved = generate_solved()
        # Maak een echte copy, niet een verwijzing. Zie bron 2
        digable = numpy.empty_like(solved)
        digable[:] = solved

        digged = dig(digable, "easy")
        draw_grid(digged, solved)


    master.title('Grid')
    entries = []

    def create_button_new_medium():
        solved = generate_solved()
        # Maak een echte copy, niet een verwijzing. Zie bron 2
        digable = numpy.empty_like(solved)
        digable[:] = solved

        digged = dig(digable, "medium")
        draw_grid(digged, solved)


    master.title('Grid')
    entries = []

    def create_button_new_difficult():
        solved = generate_solved()
        # Maak een echte copy, niet een verwijzing. Zie bron 2
        digable = numpy.empty_like(solved)
        digable[:] = solved

        digged = dig(digable, "difficult")
        draw_grid(digged, solved)

    master.title('Grid')
    entries = []





    b = 0
    for ncolumn in range(1, 10):
        for nrow in range(1, 10):
            # Voeg alle entries toe aan de entries list. Background kleuren voor zichtbaarheid
            if (ncolumn == 4 or ncolumn == 5 or ncolumn == 6) and (nrow == 1 or nrow == 2 or nrow == 3):
                entries.append(tk.Entry(master, width=3, background='grey', disabledbackground = 'grey', disabledforeground = 'orange', font=(20)))
            elif (ncolumn == 1 or ncolumn == 2 or ncolumn == 3 or ncolumn == 7 or ncolumn == 8 or ncolumn == 9) and (
                    nrow == 4 or nrow == 5 or nrow == 6):
                entries.append(tk.Entry(master, width=3, background='grey', disabledbackground = 'grey', disabledforeground = 'orange', font=(20)))
            elif (ncolumn == 4 or ncolumn == 5 or ncolumn == 6) and (nrow == 7 or nrow == 8 or nrow == 9):
                entries.append(tk.Entry(master, width=3, background='grey', disabledbackground = 'grey', disabledforeground = 'orange', font=(20)))
            else:
                entries.append(tk.Entry(master, width=3, disabledbackground = 'white', disabledforeground= 'orange', font=(100)))

            # grid layout the entries
            entries[b].grid(row=nrow, column=ncolumn)
            # bind the entries return key pressed to an action
            #tkinter.master.entries[n].bind('<Return>', partial(master.action, n))
            b += 1

    matrix_list = []
    for column in range(9):
        for row in range(9):
            matrix_list.append(matrix_digged[row][column])


    for i in range (0,81):
        if matrix_list[i] != 0:

            entries[i].insert('end', int(matrix_list[i]) )
            #Alle gegeven getallen moeten read only zijn om verwarring te voorkomen
            entries[i].configure({"state": "disabled"})

    var = tk.StringVar()
    label = tk.Label(master, textvariable=var)

    label.grid(row= 86, column = 41)

    button_1 = tk.Button(master, text="Check", command=create_button_check)
    button_1.grid(row=84, column=41)

    button_easy = tk.Button(master, text="New Easy", command=create_button_new_easy)
    button_easy.grid(row=88, column=41)

    button_medium = tk.Button(master, text="New Medium", command=create_button_new_easy)
    button_medium.grid(row=89, column=41)

    button_difficult = tk.Button(master, text="New Difficult", command=create_button_new_easy)
    button_difficult.grid(row=90, column=41)



    master.mainloop()


solved = generate_solved()



#Maak een echte copy, niet een verwijzing. Zie bron 2
digable = numpy.empty_like(solved)
digable[:] = solved

digged = dig(digable,"easy")

draw_grid(digged, solved)


