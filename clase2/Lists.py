#Declaración de listas
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f'Valores actuales de mi lista: {my_list}')

#Agregar elementos
my_list.append(0)
my_list.append(11)
print(f'Valores actuales de mi lista: {my_list}')

#Ordenar los elementos de la lista mediante el metodo sort
my_list.sort()
print(f'Valores actuales de mi lista: {my_list}')

#Modificar y eliminar un elemento
my_list[0] = 'Esta es una cadena'
my_list.pop()

print(f'Valores actuales de mi lista: {my_list}')

#Creacion de una sublista
my_sublist = my_list[0:5]
print(f'Valores actuales de mi sublista: {my_sublist}')


#Imprimir los valores de mi lista
count = 0
for item in my_list:
    print(f'Elemento de la lista {count} - {item}')
    count += 1

'''
print(f'\n\nEstos son los elementos de mi lista que serán impresos mediante un ciclo for:')
for elemento in my_list:
    print(elemento)
'''