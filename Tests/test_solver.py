import unittest
from dig_holes import *
import generate_solved as gen
import numpy

class test_solver(unittest.TestCase):
    def test_solve_puzzle(self):
        matrix = numpy.array([[9, 7, 3, 8, 6, 4, 1, 2, 5],
                            [1, 5, 8, 2, 3, 9, 4, 6, 7],
                            [2, 6, 4, 7, 1, 5, 9, 8, 3],
                            [5, 1, 9, 6, 7, 3, 2, 4, 8],
                            [6, 4, 2, 5, 9, 8, 7, 3, 1],
                            [8, 3, 7, 4, 2, 1, 5, 9, 6],
                            [3, 2, 6, 1, 4, 7, 8, 5, 9],
                            [7, 9, 5, 3, 8, 2, 6, 1, 4],
                            [4, 8, 1, 9, 5, 6, 3, 7, 2]])

        solved = numpy.array([[9, 0, 0, 8, 0, 4, 0, 2, 0],
                            [1, 0, 8, 0, 0, 0, 0, 6, 7],
                            [2, 6, 0, 7, 1, 5, 9, 8, 0],
                            [0, 1, 0, 6, 0, 3, 0, 0, 8],
                            [6, 0, 0, 0, 9, 8, 0, 0, 1],
                            [0, 0, 7, 0, 0, 0, 5, 9, 6],
                            [0, 2, 6, 0, 4, 7, 8, 5, 0],
                            [0, 0, 5, 3, 8, 0, 6, 0, 0],
                            [4, 8, 0, 0, 0, 0, 0, 7, 2]])

        self.assertTrue((solve(matrix) == solved).all)

    def test_solve_unsolvable(self):
        #Deze matrix is onoplosbaar, de functie hoort dan False terug te geven
        matrix = [
            [1, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 3, 0, 1, 0, 0, 0, 0],
            [0, 0, 4, 0, 0, 0, 0, 1, 0],
            [0, 0, 8, 0, 0, 0, 0, 0, 0]
        ]
        self.assertAlmostEqual(solve(matrix), False)