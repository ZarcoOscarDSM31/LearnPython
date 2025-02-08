#DECLARAR UN DICCIONARIO

student = {
    'name': 'Oscar Daniel',
    'age': 20,
    'languages': ['Python', 'C#', 'Java'],
    'address': {
        'street': 'Calle 1',
        'city': 'CDMX',
        'country': 'Mexico'
    },
    'is_active': True
}

# ACCEDER A LOS VALORES DE UN DICCIONARIO
print(f'Contenido del diccionario: {student}')
print(f'\nNombre: {student["name"]}')
print(f'Edad: {student["age"]}')


        #OPERACIONES BÁSICAS CON DICCIONARIOS

#MODIFICAR VALORES DE UN DICCIONARIO
student['languages'] = 'TypeScript'
print(f'\nContenido del diccionario una vez modificado: {student}')

#ELIMINAR VALORES DE UN DICCIONARIO
student.pop('address')
print(f'\nContenido del diccionario una vez eliminado: {student}')

#AGREGAR VALORES A UN DICCIONARIO
student['comida'] = 'Pizza'
print(f'\nContenido del diccionario una vez agregado: {student}')


#ITERAR UN DICCIONARIO
print(f'\n\nIterar sobre un diccionario')
print(f'Iterar de forma simple')
for element in student:
    print(f'{element}: {student[element]}')

print(f'\n\nIterar de forma destructurada - unpacking')
for key, value in student.items():
    print(f'Llave: {key}: Valor: {value}')

print(f'\n\nIterar con llave')
for key in student.keys():
    print(f'LLave: {key}')

print(f'\n\nIterar con valor')
for value in student.values():
    print(f'Valor: {value}')
