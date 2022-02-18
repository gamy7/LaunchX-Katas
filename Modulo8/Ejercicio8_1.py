#crea un diccionario
planet = { 
    'name':'Mars' ,
    'moons': '2'
}

# Muestra el nombre del planeta y el número de lunas que tiene.
print('planeta: ' + planet['name'])
print('Lunas: '+ planet['moons'])

#Agregar datos
planet['circunferencia(km)'] ={
'polar': 6752,
'equatorial': 6792
}
#imprimir nombre de planeta y su circunferencia polar
print(f'El planeta {planet["name"]}  tiene de circunferencia polar {planet["circunferencia(km)"]["polar"]}' )