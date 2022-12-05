# exrcice 6
def sommeChifre(number):
    S=0
    while (number>0):
        S+=1
        number//=10
    return S
print(sommeChifre(1875657455674))


