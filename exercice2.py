# exrcice 2

def fact(X):
    if(X<=0):
        return 1 
    else:
        fact=1
        for i in range(1,X+1):
            fact *= i
        return fact
print(fact(8))

