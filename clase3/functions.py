
def saludar():
    print(f'Hola mundo desde la funcion')
#saludar()

def sumar_numeros(numx, numy):
    suma = numx + numy
    print(f'El resultado de la suma es: {suma}')
    return suma

#Funcion con valores por defecto
def valor_defecto(numx = 10, numy = 20, numz = 5):
    suma = numx + numy + numz
    print(f'El resultado de la suma es: {suma}')
    return suma

#sumatoria = sumar_numeros(10, 20)
#print(f'La sumatoria es: {sumatoria}')
#sumatoria = valor_defecto(25, 12)

def alumnos_materias(nombre, *args):
    print(f'El alumno es: {nombre}, materias: {args}')
    print(f'El alumno es: {type(nombre)}, materias: {type(args)}')
#alumnos_materias('Oscar', 'Programación', 'Bases de Datos', 'Fisica', 'Quimica')

def alumno_calificaciones(nombre, **kwargs):
    print(f'El alumno es: [nombre], calificaciones: {kwargs}')
    print(f'El alumno es: {type[nombre]}, calificaciones: {type(kwargs)}')

alumno_calificaciones('Oscar', Programación = 10, Bases_de_Datos=9, Fisica=9, Quimica=8)