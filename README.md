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

## Instrucciones para su ejecución

El programa hace uso de la librería `numpy`, la cual está instalada en un entorno virtual de Python. Para poder acceder a ella se deberá activar el entorno virtual con el siguiente comando: `Proyecto_TC1028\Scripts\activate`.
