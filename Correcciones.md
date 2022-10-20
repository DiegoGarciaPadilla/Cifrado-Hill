# Correcciones.

En este documento se expondrán los errores que hubo en el proyecto y cómo se resolvieron para un mejor funcionamiento del mismo.

### 1. Funciones.

#### Recomendación del profesor:

*Aún puedes separar más tu código en funciones, como cuando pones " Validar si la matriz clave es invertible", es el mismo código en la función de cifrar y descifrar, pon ese código en una función separada.*

#### Código antes:

```python
while np.linalg.det(clave) == 0:
	clave = np.zeros((dimClave, dimClave))
	    for i in range(dimClave):
	      for j in range(dimClave):
	        clave[i][j] = int(input("Ingrese el valor de la posición " + str(i+1) + "," + str(j+1) + ": "))
```
#### Código después:

Se crearon las siguientes funciones:

 1. Función que comprueba si la matriz es invertible:
```python
def es_invertible(matriz):
	return  np.linalg.det(matriz) != 0
```
 2. Función que permite el llenado de la matriz:
```python
def  llenar_matriz(dim):
	matriz = np.zeros((dim, dim))
	for  i  in  range(dim):
		for  j  in  range(dim):
			matriz[i][j] = int(input("Ingrese el valor de la posición " + str(i+1) + "," + str(j+1) + ": "))
	return  matriz
```
Por lo que el código anterior resultó de la siguiente manera:
```python
while not es_invertible(clave):
	print("La matriz clave no es invertible")
	clave = llenar_matriz(dimClave)
```