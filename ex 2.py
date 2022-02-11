def lee(lista):
 return len(lista)==8 and lista.count(lista[4])>=3
 
lista = [30,500,858,7,85,56,85,85]

print(lee(lista))