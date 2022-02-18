

 #Función para leer 3 tanques de combustible y muestre el promedio

def informes(tank1, tank2, tank3):
    return (f"""     Informe 
    {'-'*70}
    Tanque 1: {tank1}
    Tanque 2: {tank2}
    Tanque 3: {tank3}
    Total promedio: {promediof(tank1, tank2, tank3)}""")


#funcion promedio
def promediof(*args):
    total_promedio= sum(args)
    n_datos= len(args)
    return total_promedio/n_datos

#print(promediof(3,3,3))

#llamamos a la funcion
print(informes(73, 88, 43))