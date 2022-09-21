# Importar librerías

import numpy as np

# Inicializar variables

abecedario = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L",
              "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", " "]

# Funciones

# Funcion de cifrado

def cifrar(mensaje, clave):

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
      mensaje_numeros = np.append(mensaje_numeros, (ord(mensaje[letra]) - 64))

  # Inicializar matriz de clave

  dimClave = int(input("Ingrese la dimensión de la clave: "))
  clave = np.zeros((dimClave, dimClave))

  # Ingresar valores de la matriz de clave

  for i in range(dimClave):
    for j in range(dimClave):
      clave[i][j] = int(input("Ingrese el valor de la posición " + str(i) + "," + str(j) + ": "))

  # Validar si la matriz clave es invertible

  while np.linalg.det(clave) == 0:
    print("La matriz clave no es invertible")
    clave = np.zeros((dimClave, dimClave))
    for i in range(dimClave):
      for j in range(dimClave):
        clave[i][j] = int(input("Ingrese el valor de la posición " + str(i) + "," + str(j) + ": "))

  # Initializar matriz de mensaje

  if len(mensaje_numeros) % dimClave != 0:
    espacios = dimClave - (len(mensaje_numeros) % dimClave)
    for i in range(espacios):
      mensaje_numeros = np.append(mensaje_numeros, 27)

  mensaje_matriz = mensaje_numeros.reshape(int(len(mensaje_numeros) / dimClave), dimClave)

  # Cifrar mensaje

  mensaje_cifrado = np.matmul(mensaje_matriz, clave)

  # Imprimir mensaje cifrado y guardar en archivo txt

  print("Mensaje cifrado: ", mensaje_cifrado.reshape(-1))

  cifrado_txt = ['''Mensaje: {mensaje} \n
  Matriz clave:
  {clave} \n
  Mensaje cifrado: 
  {mensaje_cifrado}'''.format(mensaje=mensaje, clave=clave, mensaje_cifrado=mensaje_cifrado.reshape(-1))]

  np.savetxt('cifrado.txt', cifrado_txt, fmt='%s')

# Funcion de descifrado

def descifrar(mensaje, clave):

  # Leer mensaje

  dimMensaje = int(input("Ingrese la dimensión del mensaje: "))

  for i in range(dimMensaje):
    mensaje = np.append(mensaje, int(
    input("Ingrese el valor de la posición " + str(i) + " para el mensaje: ")))

  # Inicializar matriz de clave

  dimClave = int(input("Ingrese la dimensión de la clave: "))

  if dimMensaje % dimClave != 0:
    raise ArithmeticError(f"La dimensión de la matriz código no es compatible con la longitud del mensaje")

  clave = np.zeros((dimClave, dimClave))

  # Ingresar valores de la matriz de clave

  for i in range(dimClave):
    for j in range(dimClave):
      clave[i][j] = int(input("Ingrese el valor de la posición " + str(i) + "," + str(j) + " para la matriz clave: "))

  # Validar si la matriz clave es invertible

  while np.linalg.det(clave) == 0:
    print("La matriz clave no es invertible")
    clave = np.zeros((dimClave, dimClave))
    for i in range(dimClave):
      for j in range(dimClave):
        clave[i][j] = int(input("Ingrese el valor de la posición " + str(i) + "," + str(j) + ": "))

  # Inicializar matriz de mensaje

  mensaje_matriz = mensaje.reshape(int(len(mensaje) / dimClave), dimClave)

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

  # Imprimir mensaje descifrado y guardar en archivo txt

  print("Mensaje descifrado: ", mensaje_descifrado_string)

  descifrado_txt = ['''Mensaje cifrado: {mensaje} \n
  Matriz clave:
  {clave} \n
  Mensaje descifrado: 
  {mensaje_descifrado_string}'''.format(mensaje=mensaje, clave=clave, mensaje_descifrado_string=mensaje_descifrado_string)]

  np.savetxt('descifrado.txt', descifrado_txt, fmt='%s')

# Funcion principal

def main():

  # Mensaje de bienvenida

  bienvenida = '''
              ,---------------------------,
              |  /---------------------\  |
              | |                       | |
              | |                       | |
              | |      Encriptar        | |
              | |       mensaje         | |
              | |                       | |
              |  \_____________________/  |
              |___________________________|
            ,---\_____     []     _______/------,
          /         /______________\           /|
        /___________________________________ /  | ___
        |                                   |   |    )
        |  _ _ _                 [-------]  |   |   (
        |  o o o                 [-------]  |  /    _)_
        |__________________________________ |/     /  /
    /-------------------------------------/|      ( )/
  /-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/ /
/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/ /
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'''

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

main()
