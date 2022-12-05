# exercice 3

def fact(X):
    if(X<=0):
        return 1 
    else:
        fact=1
        for i in range(1,X+1):
            fact *= i
        return fact

def sommeSerie(n):
    sommeSerie = 0
    for i in range(1, n+1):
        sommeSerie += fact(i-1)
    return sommeSerie
print(sommeSerie(4))