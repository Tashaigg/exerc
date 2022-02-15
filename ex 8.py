lista = 'The colors in my ......studyroom are blue, green, and yellow.'
novalista = ""
separadores = ""
final = []
sepa = []

for i in range(len(lista)):
   # print(i)
   # print(lista[i])
    cart = lista[i]
    if cart.isalnum() == True:
        if separadores != "":
            sepa.append(separadores)
        separadores = ""
        novalista = str(novalista) + str(cart)
    else:
        if novalista != "":
            final.append(novalista)
        novalista = ""
        separadores = str(separadores) + str(cart)

if lista[len(lista)-1].isalnum() == True:
    if novalista != "":
            final.append(novalista)
else:
    if separadores != "":
            sepa.append(separadores)


#print(separadores)
#print(novalista)
#print(len(lista))
print(final)
print(sepa)