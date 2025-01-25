print('Ejemplo de Tuplas\n\n')

#definicion de tupla
my_tuple = ('Oscar', 1,  5.5,)
print(f'información de la tupla: {my_tuple}')

#Destructuracion de tuplas
fullname, age, salalry = my_tuple

print(f'Fullname: {fullname}, Age: {age}, Salary: {salalry}')

#Impresión de tuplas con ciclo for
print(f'\n\nEstos son los elementos de mi tupla que serán impresos mediante un ciclo for:')
for element in my_tuple:
    print(element)

