#Ejercicio2 
# Agrega el código para crear nuevas variables para la velocidad y el tamaño del asteroide
# Para probar el código, prueba con varias velocidades y tamaños
# Escribe varias expresiones de prueba o combinaciones de expresiones de prueba para determinar qué mensaje se debe enviar a Tierra.

velocidadA= 20
tamanoA= 20

if velocidadA > 25 and tamanoA > 25:
    print("Advertencia, Peligro de asteroide!")
elif velocidadA >= 20 and tamanoA < 25:
    print("Mira el cielo, hay un rayo de luz ")
else:
    print("Todo tranquilo, no hay nada que ver")
