lista = input ('enter list')

print (lista)

''''
s19s = lista.count('19')
s5s = lista.count('5')

if s19s == 2:
   # print("19 ok")
    if s5s >= 3:
       # print ('5 ok')
       print('true')
    else:
       print ('false')

else:
       print ('false')
'''

def test(lista):
    return lista.count('19')==2 and lista.count('5')>=3

print(test(lista))