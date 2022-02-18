#Ejercicio 2 Modulo 4 Formateando Cadenas

#datos
from re import L
#variables
name = "Marte"
gravity = 0.00143 # in kms
planet = "Ganímedes"

#cremos el titulo
titulo= f"""Datos de gravedad en {name}""".title() 

#creamos la plantilla
cadena = f"""{"-"* 70}
Nombre del planeta: {planet}
Gravedad en {planet}: { gravity * 1000} m/s """ # metros

#union de ambas cadenas
unioncadena = f"""{titulo}
{cadena}"""
print(unioncadena)

#uso de format
print(titulo.format(name=name) + cadena.format(planet=planet, gravity=gravity))
