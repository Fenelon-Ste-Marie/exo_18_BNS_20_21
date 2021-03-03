from exercices.exercice2 import *

def test_insertion():
    assert insere(3,[1,2,4,5]) == [1, 2, 3, 4, 5]
    assert insere(10,[1,2,7,12,14,25]) == [1, 2, 7, 10, 12, 14, 25]
    assert insere(1,[2,3,4]) == [1, 2, 3, 4]
    
