lista = []

elemento1 = input('ingresa el numero 1: ')
elemento2 = input('ingresa el numero 2: ')
elemento3 = input('ingresa el numero 3: ')

lista.append(elemento1)
lista.append(elemento2)
lista.append(elemento3)

if elemento1 <= elemento2 and elemento1 <= elemento3:
    print(f'el numero menor es: {elemento1}')

elif elemento2 <= elemento1 and elemento2 <= elemento3:
    print(f'el numero menor es: {elemento2}')

else:
    print(f'el numero menor es: {elemento3}')




