lista = 'W3resource Python Exercises.'
novalista = ""
separadores = ""
final = []
sepa = []

for i in range(len(lista)):
   # print(i)
   # print(lista[i])
    cart = lista[i]
    if cart.isalnum() == True:
        sepa.append(separadores)
        separadores = ""
        novalista = str(novalista) + str(cart)
    else:
        final.append(novalista)
        novalista = ""
        separadores = str(separadores) + str(cart)






print(final)
print(sepa)