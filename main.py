'''
Autor: Diego Antonio García Padilla

El siguiente algoritmo permite al usuario ingresar un mensaje y una clave
para cifrar el mensaje, y luego ingresar el mensaje cifrado y la clave para
descifrar el mensaje.

Se asume que el mensaje a cifrar es una cadena de caracteres alfabéticos
mayúsculas y espacios, y que la clave es una matriz cuadrada invertible.

El algortmo usa la librería numpy para realizar las operaciones matriciales
necesarias para cifrar y descifrar el mensaje.

Algunas funciones de la librería numpy utilizadas son:
    - np.zeros((dim, dim)): crea una matriz de dim x dim con todos sus
    elementos iguales a 0.
    - np.array([]): crea un arreglo vacío.
    - np.append(arreglo, elemento): agrega un elemento al final del arreglo.
    - np.matmul(matriz1, matriz2): multiplica dos matrices.
    - np.linalg.det(matriz): calcula el determinante de una matriz.
    - np.linalg.inv(matriz): calcula la inversa de una matriz.
    - np.reshape(filas, columnas): redimensiona una matriz a filas x columnas.

'''

# Importar librerías

import numpy as np

# Inicializar variables

abecedario = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L",
              "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", " "]

# Funciones

# Función para comprobar si la matriz es invertible


def es_invertible(matriz):
    return np.linalg.det(matriz) != 0

# Función para llenar matriz


def llenar_matriz(dim):
    matriz = np.zeros((dim, dim))
    for i in range(dim):
        for j in range(dim):
            matriz[i][j] = int(
                input("Ingrese el valor de la posición " + str(i+1) + "," + str(j+1) + ": "))
    return matriz

# Función de impresión


def imprimir(matriz):
    matriz_plana = str(matriz.reshape(-1)
                       ).split("[")[1].split("]")[0].split(".")
    matriz_plana = [i.removeprefix('\n').removeprefix(' ')
                    for i in matriz_plana]
    mensaje = ""
    for char in matriz_plana:
        if char != '':
            mensaje += char + ", "
    return mensaje

# Funcion de cifrado


def cifrar(mensaje, clave):

    # Ingrese destinatario

    destinatario = input("Ingrese el destinatario: ")

    # Leer mensaje

    mensaje = input("Ingrese el mensaje a cifrar: ")

    # Convertir mensaje a mayúsculas

    mensaje = mensaje.upper()

    # Convertir mensaje a lista de numeros

    mensaje_numeros = np.array([])

    for letra in range(len(mensaje)):
        if ord(mensaje[letra]) == 32:
            mensaje_numeros = np.append(mensaje_numeros, 27)
        else:
            mensaje_numeros = np.append(
                mensaje_numeros, (ord(mensaje[letra]) - 64))

    # Inicializar matriz de clave

    dim_clave = int(input("Ingrese la dimensión de la clave: "))
    clave = np.zeros((dim_clave, dim_clave))

    # Ingresar valores de la matriz de clave

    for i in range(dim_clave):
        for j in range(dim_clave):
            clave[i][j] = int(
                input("Ingrese el valor de la posición " + str(i+1) + "," + str(j+1) + ": "))

    # Validar si la matriz clave es invertible

    while not es_invertible(clave):
        print("La matriz clave no es invertible")
        clave = llenar_matriz(dim_clave)

    # Initializar matriz de mensaje

    if len(mensaje_numeros) % dim_clave != 0:
        espacios = dim_clave - (len(mensaje_numeros) % dim_clave)
        for i in range(espacios):
            mensaje_numeros = np.append(mensaje_numeros, 27)

    mensaje_matriz = mensaje_numeros.reshape(
        int(len(mensaje_numeros) / dim_clave), dim_clave)

    # Cifrar mensaje

    mensaje_cifrado = np.matmul(mensaje_matriz, clave)

    # Imprimir mensaje cifrado y guardar en archivo txt

    cifrado_txt = ['Querido/a: {destinatario} \n\nEl mensaje cifrado es: {mensaje}'.format(
        destinatario=destinatario, mensaje=imprimir(mensaje_cifrado))]

    np.savetxt('cifrado.txt', cifrado_txt, fmt='%s')

    print("El mensaje cifrado se ha guardado en el archivo cifrado.txt")

# Funcion de descifrado


def descifrar(mensaje, clave):

    # Leer mensaje

    dimMensaje = int(input("Ingrese la dimensión del mensaje: "))

    for i in range(dimMensaje):
        mensaje = np.append(mensaje, int(
            input("Ingrese el valor de la posición " + str(i+1) + " para el mensaje: ")))

    # Inicializar matriz de clave

    dim_clave = int(input("Ingrese la dimensión de la clave: "))

    if dimMensaje % dim_clave != 0:
        raise ArithmeticError(
            f"La dimensión de la matriz código no es compatible con la longitud del mensaje")

    clave = np.zeros((dim_clave, dim_clave))

    # Ingresar valores de la matriz de clave

    for i in range(dim_clave):
        for j in range(dim_clave):
            clave[i][j] = int(input("Ingrese el valor de la posición " +
                              str(i+1) + "," + str(j+1) + " para la matriz clave: "))

    # Validar si la matriz clave es invertible

    while not es_invertible(clave):
        print("La matriz clave no es invertible")
        clave = llenar_matriz(dim_clave)

    # Inicializar matriz de mensaje

    mensaje_matriz = mensaje.reshape(int(len(mensaje) / dim_clave), dim_clave)

    # Descifrar mensaje

    clave_inversa = np.linalg.inv(clave)
    mensaje_descifrado = np.matmul(mensaje_matriz, clave_inversa)
    mensaje_descifrado = np.round(mensaje_descifrado)
    mensaje_descifrado = mensaje_descifrado.astype(int)
    mensaje_descifrado = mensaje_descifrado.reshape(-1)

    # Guardar mensaje descifrado en string

    mensaje_descifrado_string = ""

    for i in range(len(mensaje_descifrado)):
        mensaje_descifrado_string += abecedario[int(mensaje_descifrado[i]) - 1]

    # Guardar mensaje descifrado en archivo txt

    descifrado_txt = ['El mensaje descifrado es: {mensaje}'.format(
        mensaje=mensaje_descifrado_string)]

    np.savetxt('descifrado.txt', descifrado_txt, fmt='%s')

    print("El mensaje descifrado se ha guardado en el archivo descifrado.txt")

# Funcion principal


def main():

    # Mensaje de bienvenida

    bienvenida = '''
  
█▀▀ █▀█ █▀▄ █ █▀▀ █▀█   █▀▀ █▄░█ █ █▀▀ █▀▄▀█ ▄▀█
█▄▄ █▄█ █▄▀ █ █▄█ █▄█   ██▄ █░▀█ █ █▄█ █░▀░█ █▀█
'''

    print(bienvenida)

    # Inicializar variables

    mensaje_str = ""
    mensaje_array = np.array([])
    clave = np.array([])

    # Ingresar opcion

    opcion = int(input("Ingrese 1 para cifrar o 2 para descifrar: "))

    # Validar opcion

    while opcion != 1 and opcion != 2:
        opcion = int(input("Ingrese 1 para cifrar o 2 para descifrar: "))

    # Llamar a la funcion de cifrado o descifrado

    if opcion == 1:
        cifrar(mensaje_str, clave)
    else:
        descifrar(mensaje_array, clave)

# Llamar a la funcion principal


repetir = True
while repetir:
    main()
    repetir = int(input("Ingrese 1 para repetir el programa o 0 para salir: "))
