# exrcice 9
def bubbleSort(list):
    for i in range(len(list)-1):
        for j in range(len(list)-1):
            if (list[j]>list[j+1]):
                temp = list[j]
                list[j] = list[j+1]
                list[j+1] = temp
    return list

def puissance(X,n):
    puissance = 1
    for i in range (n):
        puissance *= X
    return puissance


# la moyenne

def moyenne (list):
    somme = 0
    for i in list:
        somme += i
    return somme / len(list)

list = [1,3,8,9]
print(moyenne(list)) # c'est juste pour tester avec des nombres réels 

# le min ou max selon le choix de l ‘utilisateur
def MinMax(list,choix):
    if choix == "min":
        min = list[0]
        for i in range (1,len(list)):
            if(min>list[i]):
                min = list[i]
        return min 
    elif choix == "max":
        max = list [0]
        for i in range (1,len(list)):
            if ( max<list[i]):
                max = list [i]
        return max 
    else :
        return " le choix est invalide"
print (MinMax(list,"min"))

# fonction qui renvoie le médian d‘une liste
 

def médiane(list):
    sort = bubbleSort(list)
    if (len(list)%2 == 0):
        res1 = sort [len(list)//2-1]
        res2 = sort [len(list)//2]
        return (res1+res2)/2

    else:
        return sort[len(list)//2]
print("la mediane est de :  ",médiane(list))

# le mode 

def Mode(list):
    return MinMax(list,"max")
print ("le mode est : " ,Mode(list))

# la variance 

def Variance(list):
    somme=0
    for i in range(len(list)):
        somme+= puissance(list[i],2)
    return somme/len(list) - puissance(moyenne(list),2)
print ("la variance est de : " , Variance(list))
