# Función con un informe preciso de la misión. 
# Considera hora de prelanzamiento, tiempo de vuelo, destino, tanque externo y tanque interno

def informe(destino, *minutos,  **fuel_reservoirs):
    datos= f"""  Informe
    {'-'*70} 
    Destino: {destino}
    Tiempo de vuelo hasta destino: {sum(minutos) } 
    Combustible izquierdo total: {sum(fuel_reservoirs.values())}"""
    #mostrar nombres de tanques
    for tanques, combustible in fuel_reservoirs.items():
        datos += f"""
        Tanque {tanques} : {combustible}"""
    return datos


print(informe("Venus", 12, 47,  interno=400000, externo=500000))
