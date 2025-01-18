#otros metodos

message = "Los cuervos de la UTVT"

#len
size = len(message)

#replace
message = message.replace("UTVT", "UVM")

#find
position = message.find("U")

#split
words = message.split(" ")


print("MENSAJE: ", message)
print("El tamaño es: ", size)
print("Reemplazo: ", message)
print("Posicion: ", position)
print("Palabras: ", words)
