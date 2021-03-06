from Algorithmic.solver import *
import random
from tools import *
import numpy

#Deze functie zoekt de volgende cel die gedugt kan worden
def find_next(dict, dif):
    #Lijst met keys(coordinaten) die kunnen worden gedugt
    dugable = []
    for key, value in dict.items():
        if value == 1:
            dugable.append(key)

    if len(dugable) == 0:
        return None


    return random.choice(dugable)

#Deze functie checkt of de cel gedugt mag worden
def check_valid(matrix, row, column, dif):
    correct_num = matrix[row,column]
    nums = [1,2,3,4,5,6,7,8,9]
    nums.remove(correct_num)

    subgrid = get_subgrid(row,column)

    subgrids = matrix_to_subgrids(matrix)

    #Eerst moet er gekeken worden of als je deze cel dugt je een restrictie verbreekt (operation 2)

    #Regels per moeilijkheidsgraad
    if dif == "easy":
        # Het totaal aantal gegeven getallen moet tussen deze twee getallen zitten
        min_givens = 36
        max_givens = 49
        #Het aantal gegevens per rij en kolom moet hoger of gelijk zijn dan dit getal
        min_givens_rowcol = 4

    elif dif == "medium":
        min_givens = 32
        max_givens = 35
        min_givens_rowcol = 3

    elif dif == "difficult":
        min_givens = 28
        max_givens = 31
        min_givens_rowcol = 2

    #Als niet aan de bovenstaande regels voldaan wordt dan mag de cel niet leeggemaakt worden
    randomized_bound = random.randrange(min_givens, max_givens)

    #Als er minder totaal gegeven getallen zijn dan toegestaan
    if numpy.count_nonzero(matrix) <= randomized_bound:
        return False

    # Als er minder totaal gegeven getallen per rij of kolom zijn dan toegestaan
    elif numpy.count_nonzero(matrix[row]) <= min_givens_rowcol or numpy.count_nonzero(matrix[:, column]) <= min_givens_rowcol:
        return False


    #Voor elk ander getal dan het getal wat je weg gaat halen mag er GEEN oplossing zijn als je die in de cel invult die je weg wil halen
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

    #Wordt aan alle regels voldaan? Dan mag de cel leeggemaakt worden
    return True

#Deze functie haalt getallen weg op basis van moeilijkheidsgraad
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


        







