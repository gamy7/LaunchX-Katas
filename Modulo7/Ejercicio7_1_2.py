# Declara dos variables
new_planet = ''
planets = []
# Escribe el ciclo while solicitado
while new_planet.lower() != 'done':
    if new_planet:
        planets.append(new_planet)
    new_planet = input('Ingresa un nuevo planeta o done para terminar: ')

#Ejercicio 2
#Escribe tu ciclo for para iterar en una lista de planetas
for planet in planets:
    print(planet)