
lista = [1, 2, 1, 1, 1, 2, 1, 4, 1, 2, 1, 4, 1, 2, 1, 4, 1, 2, 3, 4, 2, 3]
pop = piot= 52



def test (lista):
    m=0
    a=b=c=d=lista[0]
    n=0
    while b==a:
        n=n+1
        b = c = d = lista[n]
    while c==b or c==a:
        n=n+1
        c = d = lista[n]
    while d==c or d==b or d==a:
        n=n+1
        d = lista[n]
    
    print(f' valor a: {a}')
    print(f' valor b: {b}')
    print(f' valor c: {c}')
    print(f' valor d: {d}')
 
    
    for i in range(len(lista)):
        print(i)
        if (lista[i] != a and lista[i] != b and lista[i] != c and lista[i] != d):
            print ('Quinto elemento')
            break
        else:
            if (type(lista[i]))!=int:
                print('wrong type')
                break
            else:
                if i >= 20:
                    print('verificado 20 números')
                    break
                else:
                    if lista[i] == m:
                        print ('Números cosnecutivos')
                        break
                    else:
                        m = lista[i]
                        print('all cool')
    
test(lista)


