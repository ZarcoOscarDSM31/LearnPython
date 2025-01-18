#Elif statement

age = int(input("Ingrese su edad: "))

if age < 12:
    print("Eres un niño")
elif age < 17:
    print("Eres adolescente")
elif age <= 35:
    print("Eres adulto joven")
else:
    print("Eres un adulto")