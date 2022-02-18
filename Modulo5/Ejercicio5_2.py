# Almacenar las entradas del usuario
distancia_planeta1 = input("Escribe la distancia al sol del planeta 1: ")


distancia_planeta2 = input("Escribe la distancia al sol del planeta 2: ")

# Convierte las cadenas de ambos planetas a números enteros
distancia_planeta1 = int(distancia_planeta1)
distancia_planeta2 = int(distancia_planeta2)
# Realizar el cálculo y determinar el valor absoluto
distancia= distancia_planeta2- (distancia_planeta1)#km
print(distancia)
# Convertir de KM a Millas
distancia_millas = distancia * 0.621 # millas
print(abs(distancia_millas))
