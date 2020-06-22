import unittest
from Algorithmic.dig_holes import *
from Algorithmic import generate_solved as gen
import numpy

class TestDig_easy(unittest.TestCase):
    def test_dig_easy_totalgivens(self):
        #test of de dig functie voor elke moeilijkheidsgraad het correcte aantal totale gegeven getallen geeft
        matrix = gen.generate_solved()
        matrix_dig = dig(matrix, "easy")
        nonzero = numpy.count_nonzero(matrix_dig)
        self.assertTrue( 49>=nonzero >=36)

    def test_dig_easy_rowcol(self):
        # test of de dig functie voor elke moeilijkheidsgraad het correcte aantal gegeven getallen geeft per rij en kolom
        matrix = gen.generate_solved()
        matrix_dig = dig(matrix, "easy")
        list_givens = []
        for row in range(0, 9):
            list_givens.append(numpy.count_nonzero(matrix_dig[row]))
        for col in range(0, 9):
            list_givens.append(numpy.count_nonzero(matrix_dig[col]))
        list_2 = [i for i in list_givens if i < 4]
        self.assertAlmostEqual(len(list_2), 0)


class TestDig_medium(unittest.TestCase):
    def test_dig_medium_totalgivens(self):
        #test of de dig functie voor elke moeilijkheidsgraad het correcte aantal totale gegeven getallen geeft
        matrix = gen.generate_solved()
        matrix_dig = dig(matrix, "medium")
        nonzero = numpy.count_nonzero(matrix_dig)
        self.assertTrue( 35>=nonzero >=32)

    def test_dig_medium_rowcol(self):
        #test of de dig functie voor elke moeilijkheidsgraad het correcte aantal gegeven getallen geeft per rij en kolom
        matrix = gen.generate_solved()
        matrix_dig = dig(matrix, "medium")
        list_givens = []
        for row in range(0,9):
            list_givens.append(numpy.count_nonzero(matrix_dig[row]))
        for col in range(0, 9):
            list_givens.append(numpy.count_nonzero(matrix_dig[col]))
        list_2 = [i for i in list_givens if i < 3]
        self.assertAlmostEqual(len(list_2), 0)

class TestDig_difficult(unittest.TestCase):
    def test_dig_difficult_totalgivens(self):
        #test of de dig functie voor elke moeilijkheidsgraad het correcte aantal totale gegeven getallen geeft
        matrix = gen.generate_solved()
        matrix_dig = dig(matrix, "difficult")
        nonzero = numpy.count_nonzero(matrix_dig)
        self.assertTrue(31 >= nonzero >= 28)

    def test_dig_difficult_rowcol(self):
        #test of de dig functie voor elke moeilijkheidsgraad het correcte aantal gegeven getallen geeft per rij en kolom
        matrix = gen.generate_solved()
        matrix_dig = dig(matrix, "difficult")
        list_givens = []
        for row in range(0,9):
            list_givens.append(numpy.count_nonzero(matrix_dig[row]))
        for col in range(0, 9):
            list_givens.append(numpy.count_nonzero(matrix_dig[col]))
        list_2 = [i for i in list_givens if i < 2]
        self.assertAlmostEqual(len(list_2), 0)


