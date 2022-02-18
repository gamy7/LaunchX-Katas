# Ejercicio1 modulo 4 Transformar cadenas

text = """Interesting facts about the Moon. The Moon is Earth's only satellite. There are several interesting facts about the Moon and how it affects life here on Earth. 
On average, the Moon moves 4cm away from the Earth every year. This yearly drift is not significant enough to cause immediate effects on Earth. The highest daylight temperature of the Moon is 127 C."""

#Divide el texto en cada oración
dividir = text.split(".")
print(dividir)

#Define algunas palabras clave para búsqueda para determinar si una oración contiene un hecho.
pclave= ["average", "temperature", "distance"]

#bucle para imprimir  datos sobre la Luna que estén relacionados con las palabras clave definidas

for oracion in dividir:
    for clave in pclave:
        if clave in oracion:
            print(oracion)

# Ciclo para cambiar C a Celsius
for oracion in dividir:
    for clave in pclave:
        if clave in oracion:
            # Ciclo para cambiar C a Celsius
            print(oracion.replace('C', 'Celsius'))
           





