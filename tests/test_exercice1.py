from exercices.exercice1 import *

def test_mini():
    t_moy = [14.9, 13.3, 13.1, 12.5, 13.0, 13.6, 13.7]
    annees = [2013, 2014, 2015, 2016, 2017, 2018, 2019]
    resultat = mini(t_moy,annees) 
    assert resultat  == (12.5, 2016) 

