# Lista de planetas
planets = ['Mercurio', 'Venus', 'Tierra', 'Marte', 'Jupiter', 'Saturno', 'Neptuno']
print("Planetas: " + str(planets))
#Solicitamos el nombre de un planeta
seleccion_planeta = input("Ingresa el planeta de elegido: ")
# Busca el planeta en la lista
seleccion_index = planets.index(seleccion_planeta)
# Muestra los planetas más cercanos al sol
print("Los planetas mas cercanos a "+ seleccion_planeta +" son : " + str(planets[0:seleccion_index]))
#Muestra los planetas mas lejanos del sol
print("Los planetas mas lejanos a "+ seleccion_planeta +" son : " + str(planets[seleccion_index+1:]))
