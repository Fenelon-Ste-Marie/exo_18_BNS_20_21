from exercices.exercice2 import *

def test_inversion():
    chaine='bac'
    assert inverse_chaine(chaine) == 'cab'
    
def test_palindrome():
    chaine='NSI'
    assert est_palindrome(chaine) ==False

def test_nbre_palindrome():
    assert est_nbre_palindrome(214312) == False
    assert est_nbre_palindrome(213312) == True
