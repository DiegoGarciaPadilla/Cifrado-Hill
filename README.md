# Proyecto_TC1028

_Proyecto para el módulo de Pensamiento Computacional Para Ingeniería_

[Archivo de correcciones](Correcciones.md)

## Descripción.

Algoritmo que permite al usuario codificar y decodificar mensajes mediante el cifrado de Hill, para después imprimir los resultados en consola y, además, guardarlos en un archivo tipo txt.

### Cifrado de Hill.

Supongamos que se tiene una matriz invertible $A$ (matriz de codificación) y un texto que se quiere cifrar.

Transformamos el texto a una secuencia de números, dando a cada carácter un valor numérico único; a continuación, formamos una matriz mediante la agrupación de los números en columnas de acuerdo al orden de la matriz A (la cantidad de elementos en cada columna debe ser igual al orden de la matriz). Llamemos a esta matriz B (la matriz plana). Multipliquemos la matriz A por la matriz B:

$$C = A \cdot B$$

La matriz $C$ es la matriz cifrada.

Para descifrar el mensaje, sólo debe multiplicarse $A^{-1} \cdot C$, donde $A^{-1}$ es la matriz inversa de $A$.

Nótese que:

$$A^{-1} \cdot C = A^{-1} \cdot A\cdot B = I \cdot B = B$$

El texto plano original se puede hallar nuevamente tomando la matriz resultante y uniendo sus vectores columna, de manera que formen una secuencia, para luego convertir los números en los caracteres respectivos.

### Algoritmo

```
1. Leer mensaje
2. mensaje_numeros = []
3. Por Cada letra en mensaje:
    3.1 numero = Codigo ASCII de la letra - 64
    3.2 Añadir numero a mensaje numeros
4. Leer dimension_clave
5. clave = []
6. i = 0
7. j = 0
8. Mientras i < dimension_clave:
    8.1 Mientras j < dimension_clave:
        8.1.1 Leer numero_clave
        8.1.2 Añadir numero_clave a la fila i, columna j, de clave
        8.1.3 j = j + 1
    8.2 i = i + 1
9. mensaje_matriz = mensaje_numeros en n columnas
10. cifrado = []
11. i = 0
12. j = 0
13. Mientras i < filas de mensaje_matriz:
    13.1 Mientras j < columnas de clave:
        13.1.1 cifrado[i][j] = 0
        13.1.2 k = 0
        13.1.3 Mientras k < filas de clave:
            13.1.3.1 cifrado[i][j] = -cifrado[i][j] + mensaje_matriz[i][j] * clave[i][j]
            13.1.3.2 k = k + 1
        13.1.4 j = j + 1
    13.2 i = i + 1
14. Imprimir cifrado
```

## Instrucciones para su ejecución

El programa hace uso de la librería `numpy`, la cual está instalada en un entorno virtual de Python. Para poder acceder a ella se deberá activar el entorno virtual con el siguiente comando: `Proyecto_TC1028\Scripts\activate`.