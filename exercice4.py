# exrcice 4
a=int (input("entrer un nombre : "))
def decimalToBinairy(number):
    if number==0 :
        return 0
    else :
        result =""
        while(number>0):
            r= number % 2
            result= str(r) + result
            number//= 2
    return int(result)
print(decimalToBinairy(a))


