# exercice 7
# ecrire une fonction Python pour trouver la fréquence d’un caractère dans une chaîne

def fréquence(str,caractére):
     count = 0
     for i in str:
        if(i == caractére):
            count += 1
        return count