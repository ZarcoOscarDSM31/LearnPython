#Definir ejemplos de colecciones
first_set = {1, 2, 3, 4, 5}
second_set = {3, 6, 7, 8, 9, 10}

#Imprimir contenido de una selección en una colección tipo SET
print(f'Mi colección tipo SET es: {type(first_set)}')

#Remover elementos de una colección
first_set.remove(5)
print(f'Mi colección actualizada: {first_set}')


#Agregar elementos a una colección
first_set.add('Hola mundo')
print(f'Mi colección actualizada ADD: {first_set}')

#Imprimir mediante ciclo for
for elemento in first_set:
    print(elemento)


#Operaciones con colecciones
union_set = first_set.union(second_set)
intersection_set = first_set.intersection(second_set)
diference_set = first_set.difference(second_set)

print(f'Union: {union_set}')
print(f'Intersección: {intersection_set}')
print(f'Diferencia: {diference_set}')