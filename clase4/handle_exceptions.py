result = None
x = 10
y = 0

try:
    numero_x = int(input('Ingrese el primer numero: '))
    numero_y = int(input('Ingrese el segundo numero: '))
    result = numero_x / numero_y

    print(f'El resultado es: {result}')

except Exception as e:
    print(f'Exception, error: {e}')
finally:
    print('Finally block')

"""
except ZeroDivisionError as e:
    print(f'Exception, error: {e}')
except ValueError as e:
    print(f'Value error, error: {e}')
"""