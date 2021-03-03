from exercices.exercice2 import *

def test_inverse_chaine():
    chaine='bac'
    assert inverse_chaine(chaine) == 'cab'
    
def test_est_palindrome():
    chaine='NSI'
    assert est_palindrome(chaine) ==False

def test_est_nbre_palindrome():
    assert est_nbre_palindrome(214312) == False
    assert est_nbre_palindrome(213312) == True
    
