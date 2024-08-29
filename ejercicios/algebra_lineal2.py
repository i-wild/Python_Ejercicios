import numpy as np
import fractions

# Configuración para imprimir como fracciones
np.set_printoptions(formatter={'all': lambda x: str(
    fractions.Fraction(x).limit_denominator())})

# Función para leer una matriz cuadrada del usuario
def leer_matriz_cuadrada(n):
    matriz = []
    for i in range(n):
        fila = input(f"Ingrese la fila {i+1} de la matriz (separada por espacios): ")
        fila = list(map(float, fila.split()))
        if len(fila) != n:
            raise ValueError("Cada fila debe tener exactamente {} elementos.".format(n))
        matriz.append(fila)
    return np.array(matriz)

# Función para leer un vector del usuario
def leer_vector(n):
    vector = input(f"Ingrese los {n} elementos del vector (separados por espacios): ")
    vector = list(map(float, vector.split()))
    if len(vector) != n:
        raise ValueError("El vector debe tener exactamente {} elementos.".format(n))
    return np.array(vector)

try:
    # Instrucciones para el usuario
    print("Este programa resolverá un sistema de ecuaciones lineales de la forma Ax = b.")
    print("Debe ingresar una matriz cuadrada A y un vector b.")
    print("La dimensión de la matriz cuadrada será n x n y el vector tendrá n elementos.")
    print()

    # Leer la dimensión de la matriz
    n = int(input("Ingrese la dimensión de la matriz cuadrada (n x n): "))
    if n <= 0:
        raise ValueError("La dimensión de la matriz debe ser un número entero positivo.")

    # Leer la matriz A
    print(f"Ingrese los elementos de la matriz A (dimensión {n}x{n}):")
    A = leer_matriz_cuadrada(n)

    # Leer el vector b
    print(f"Ingrese los elementos del vector b (dimensión {n}):")
    b = leer_vector(n)

    # Calculamos el determinante
    determinante = np.linalg.det(A)
    print(f'El determinante es: {determinante}')
    print()
    
    # Umbral para considerar el determinante como cero
    tolerance = 1e-10
    
    # Matriz no singular
    if abs(determinante) > tolerance:
        print('Solución del sistema:')
        x = np.linalg.solve(A, b)
        print(x)
        print()

        print('Comprobamos que A * x = b')
        print(np.matmul(A, x))
    else:
        print('La matriz es singular o cercana a ser singular')
except np.linalg.LinAlgError as e:
    print(f'Error en álgebra lineal: {e}')
except ValueError as e:
    print(f'Error en los datos ingresados: {e}')
except Exception as e:
    print(f'Ha ocurrido una excepción: {e}')
