from exercices.exercice1 import *

def test_recherche():
    assert recherche(1, [2, 3, 4]) == -1
    assert recherche(1, [10, 12, 1, 56]) == 2
    assert recherche(50, [1, 50, 1]) == 1
    assert recherche(15, [8, 9, 10, 15]) == 3
