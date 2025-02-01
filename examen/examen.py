
print("Ingresa tu nombre:")
name = input()

num_materias = int(input("Ingresa el número de materias: "))

calificaciones = []

for i in range(num_materias):
    calificacion = float(input(f"Ingresa la calificación de la materia #{i + 1}: "))
    calificaciones.append(calificacion)

promedio = sum(calificaciones) / num_materias

print(f"{name.title()} El promedio de su socarcuatrimestre: {promedio:.2f}")