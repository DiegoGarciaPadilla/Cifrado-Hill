# Importar librerías

import numpy as np

# Inicializar variables

abecedario = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", " "]

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

txt = ['''Mensaje: {mensaje} \n
Matriz clave:
{clave} \n
Mensaje cifrado: 
{mensaje_cifrado}'''.format(mensaje=mensaje, clave=clave, mensaje_cifrado=mensaje_cifrado.reshape(-1))]

np.savetxt('resultados.txt', txt, fmt='%s')