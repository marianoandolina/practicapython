def cuenta_regresiva(number):
    number -= 1
    if number > 0:
        print(number)
        cuenta_regresiva(number)

cuenta_regresiva(11) 

"""
Las funciones recursivas se llaman a si mismas dentro de la funcion
No son lo ideal en la programacion. 
"""            



