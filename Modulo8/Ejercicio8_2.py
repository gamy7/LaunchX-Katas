# Planets and moons

from __future__ import division


planet_moons = {
    'mercury': 0,
    'venus': 0,
    'earth': 1,
    'mars': 2,
    'jupiter': 79,
    'saturn': 82,
    'uranus': 27,
    'neptune': 14,
    'pluto': 5,
    'haumea': 2,
    'makemake': 1,
    'eris': 1
}
# Añade el código para determinar el número de lunas y el numero de planetas.
moons= planet_moons.values()
planets= len(planet_moons.keys())


# Agrega el código para contar el número de lunas
total_lunas= 0
for moon in moons:
    total_lunas= total_lunas + moon
print(f'El numero total de lunas es {total_lunas} ')

# calculo de promedio 
division= total_lunas/ planets
print(f'El promedio de lunas es {division}')