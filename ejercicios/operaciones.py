# En principio el alumno solo recibiría la definición de la función en el archivo correspondiente
def suma(x,y):

    # El alumno deberá implementar correctamente el código de la función para pasar el test correspondiente
    return x + y

#Función para saber si un número es par
def numero_par(n):
    if n % 2 == 0:
        return n, "es par."
    else:
        return n, "es impar."
