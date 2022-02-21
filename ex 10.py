#lista = ('( ()) ((()()())) (()) ()')
lista = ('() (( ( )() ( )) ) ( ())')
pop = [10,11,12,13,14]


print(len(lista))
lista=lista.replace(' ','')
print(lista)
print(len(lista))

final = []
x=""
c=0
for i in range(len(lista)):
    
    if lista[i] == '(':
        c=1+c
    elif lista[i] == ')':
        c=c-1
    x=x+lista[i]
    print(i)
    print(x)
    print(c)
    if c==0:
        final.append(x)
        x=''


print(final)