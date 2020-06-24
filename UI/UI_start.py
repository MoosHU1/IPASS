'''Bron 1 create_grid: https://www.daniweb.com/programming/software-development/threads/446765/making-multiple-entry-matrixxes-in-a-for-loop
Bron 2: https://stackoverflow.com/questions/6431973/how-to-copy-data-from-a-numpy-array-to-another
'''


import tkinter as tk
from Algorithmic.dig_holes import *
from Algorithmic.generate_solved import *

master = tk.Tk()
master.geometry("600x400")



#Functie maakt de knoppen en het veld met entries aan
def draw_grid(matrix_digged,matrix_answer):
    def create_button_check():
        # b = tk.Button(master, text="OK")
        # b.grid()
        #Haalt alle ingevulde getallen van de gebruiker op en de gegeven getallen, oftewel alle getallen die je op dat moment ziet tijdens het spelen
        #Deze worden in een lijst gezet en vervolgens in een matrix omgezet
        #Als er geen getal is ingevuld in een vakje komt daar een 0, 0 wordt gebruikt voor een leeg vakje.
        entries_get = []
        for i in range(0, 81):
            if entries[i].get() != "":
                entries_get.append(int(entries[i].get()))
            else:
                entries_get.append(0)

        user_input = entries_to_matrix(entries_get)

        #Correct is de variabele die aangeeft of de sudoku helemaal goed is(True) of dat er een fout in zit(False)
        correct = True

        #Per cel wordt er gekeken of hij gelijk is aan matrix_answer(De compleet ingevulde sudoku)
        #Eerst wordt er gecheckt of de cel niet gelijk is aan 0, dus leeg is.
        #Als er éen fout in zit dan is de sudoku incorrect en wordt correct op false gezet en voor de gebruiker het label op "Fout" gezet
        for row in range(0,9):
            for column in range(0,9):
                if user_input[row][column] != 0 and matrix_answer[row][column] != user_input[row][column]:
                    label.config(fg="red")
                    correct=False
                    var.set("")
                    var.set("Fout")

        #Als het helemaal correct is wordt er eerst nog gecheckt of alles is ingevuld, dan is de puzzel klaar en verandert het label naar "Gehaald!!"
        #Als alles wat tot nu toe is ingevuld correct is wordt het label omgezet naar "Goed"
        if correct:
            print(numpy.count_nonzero(user_input == 0))
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
    #In deze for loop worden alle tkinter entry vakken, dus de sudoku cellen toegevoegd aan een lijst genaamd entries
    for ncolumn in range(1, 10):
        for nrow in range(1, 10):
            # Voeg alle entries toe aan de entries list. Background kleuren voor zichtbaarheid
            #Disabledforeground is de kleur van de getallen als het een gegeven getal is, dit is voor duidelijkheid.
            if (ncolumn == 4 or ncolumn == 5 or ncolumn == 6) and (nrow == 1 or nrow == 2 or nrow == 3):
                entries.append(tk.Entry(master, width=3, background='grey', disabledbackground = 'grey', disabledforeground = 'orange', font=(20)))
            elif (ncolumn == 1 or ncolumn == 2 or ncolumn == 3 or ncolumn == 7 or ncolumn == 8 or ncolumn == 9) and (
                    nrow == 4 or nrow == 5 or nrow == 6):
                entries.append(tk.Entry(master, width=3, background='grey', disabledbackground = 'grey', disabledforeground = 'orange', font=(20)))
            elif (ncolumn == 4 or ncolumn == 5 or ncolumn == 6) and (nrow == 7 or nrow == 8 or nrow == 9):
                entries.append(tk.Entry(master, width=3, background='grey', disabledbackground = 'grey', disabledforeground = 'orange', font=(20)))
            else:
                entries.append(tk.Entry(master, width=3, disabledbackground = 'white', disabledforeground= 'orange', font=(100)))

            #Hier worden de cellen aan het tkinter grid toegevoegd
            entries[b].grid(row=nrow, column=ncolumn)
            b += 1

    #Zet de gegenereerde sudoku puzzel van een matrix om in een lijst, om het makkelijk in de tkinter entries in te kunnen vullen
    matrix_list = []
    for column in range(9):
        for row in range(9):
            matrix_list.append(matrix_digged[row][column])

    #Vul alle gegeven getallen in in de entry velden
    for i in range (0,81):
        if matrix_list[i] != 0:
            entries[i].insert('end', int(matrix_list[i]) )
            #Alle gegeven getallen moeten read only zijn om verwarring te voorkomen, ze hebben ook een andere kleur
            entries[i].configure({"state": "disabled"})

    var = tk.StringVar()

    #Label die na het drukken op de check knop aangeeft of je ingevulde getallen goed of fout zijn
    label = tk.Label(master, textvariable=var)

    label.grid(row= 86, column = 41)

    button_1 = tk.Button(master, text="Check", command=create_button_check)
    button_1.grid(row=84, column=41)

    button_easy = tk.Button(master, text="New Easy", command=create_button_new_easy)
    button_easy.grid(row=88, column=41)

    button_medium = tk.Button(master, text="New Medium", command=create_button_new_medium)
    button_medium.grid(row=89, column=41)

    button_difficult = tk.Button(master, text="New Difficult", command=create_button_new_difficult)
    button_difficult.grid(row=90, column=41)



    master.mainloop()


solved = generate_solved()



#Maak een echte copy, niet een verwijzing. Zie bron 2
digable = numpy.empty_like(solved)
digable[:] = solved

digged = dig(digable,"easy")

draw_grid(digged, solved)


