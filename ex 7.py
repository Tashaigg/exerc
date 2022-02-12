#lista=[0, 1, 2, 3, 4, 5]
lista=[1, 1, 1, 1, 1, 1]
#lista=[2, 2, 2, 2, 2]

'''def test (lista):
    soma=lista[0]
    for num in range(1,len(lista)):
        soma= soma + lista[num]
        if soma != num+1:
            return False
        print(soma)
    return True'''


def test (lista):
    return all ([sum(lista[:i]) == i for i in range(len(lista))])

    
print (test(lista))


