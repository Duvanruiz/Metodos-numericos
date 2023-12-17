import math
import sys

def secant_method(equation, x0, x1, epsilon, max_iter):
    # Convertir la ecuación a una función
    def f(x):
        return eval(equation, {'x': x, 'sin': math.sin, 'cos': math.cos, 'tan': math.tan, 'log': math.log})

    # Inicializar el contador de iteraciones
    iter_count = 0

    # Repetir mientras la diferencia sea mayor que el umbral y no se supere el máximo de iteraciones
    while True:
        # Calcular la siguiente aproximación usando el método de la secante
        x2 = x1 - f(x1) * (x1 - x0) / (f(x1) - f(x0))
        
        # Imprimir la iteración actual
        print(f"Iteración {iter_count + 1}: Aproximación = {x2:.5f}")

        # Actualizar las estimaciones y la diferencia
        x0, x1, diff = x1, x2, abs(x2 - x1)

        # Incrementar el contador de iteraciones
        iter_count += 1

        # Verificar las condiciones de salida
        if diff <= epsilon or iter_count >= max_iter:
            break

    # Devolver la estimación final y el número de iteraciones
    return x2, iter_count

# Ingresar la ecuación
try:
    equation = input("Ingrese la ecuación en términos de 'x': ")
except (SyntaxError, NameError):
    print("Error en la entrada de la ecuación. Por favor, verifique la sintaxis.")
    sys.exit()  # Salir del programa

# Ingresar las dos estimaciones iniciales (x0 y x1)
try:
    x0 = float(input("Ingrese la primera estimación inicial (x0): "))
    x1 = float(input("Ingrese la segunda estimación inicial (x1): "))
except ValueError:
    print("Error en la entrada. Asegúrese de ingresar números para las estimaciones iniciales.")
    sys.exit()  # Salir del programa

# Elegir el umbral y el máximo de iteraciones
epsilon = 0.00001
max_iter = int(input("Ingrese el máximo de iteraciones: "))

# Llamar a la función del método de la secante
root, iter_count = secant_method(equation, x0, x1, epsilon, max_iter)

# Imprimir el resultado final
print(f"\nLa raíz es {root:.5f}, encontrada en {iter_count} iteraciones.")
