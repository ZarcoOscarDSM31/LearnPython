#entrada de datos mediante consola

name = input("Ingrese su nombre: ")
age = int(input("Ingrese su edad: "))
salary = float(input("Ingrese su salario: "))
total_pets = eval(input("Ingrese la cantidad de mascotas: "))
university = input("Ingrese su universidad: ")

print("Su nombre es: ", name, "Su edad es: ", age, "Su universidad es: ", university)
print(type(name))
print(type(age))
print(type(salary))
print(type(total_pets))
