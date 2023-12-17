import math
import sys

def bisection_method(equation, a, b, epsilon, max_iter):
    # Convertir la ecuación a una función
    def f(x):
        try:
            result = eval(equation, {'x': x, 'sin': math.sin, 'cos': math.cos, 'tan': math.tan, 'log': math.log})
            return float(result.real)  # Obtener la parte real del resultado
        except (ValueError, TypeError):
            print("Error al evaluar la función. Asegúrate de que la ecuación sea válida.")
            sys.exit()

    # Inicializar el contador de iteraciones
    iter_count = 0

    # Verificar el signo de los extremos
    if f(a) * f(b) > 0:
        print("La función no cambia de signo en el intervalo dado. El método de bisección no puede garantizar la convergencia.")
        sys.exit()

    # Iterar según el criterio de parada
    while True:
        # Calcular el punto medio
        c = (a + b) / 2

        # Imprimir la iteración actual
        print(f"Iteración {iter_count + 1}: Aproximación = {c:.5f}")

        # Verificar el criterio de parada
        if abs(f(c)) < epsilon or iter_count >= max_iter:
            break

        # Actualizar el intervalo
        if f(c) * f(a) < 0:
            b = c
        else:
            a = c

        # Incrementar el contador de iteraciones
        iter_count += 1

    # Devolver la estimación final y el número de iteraciones
    return c, iter_count



# Ingresar la ecuación
try:
    equation = input("Ingrese la ecuación en términos de 'x': ")
except (SyntaxError, NameError):
    print("Error en la entrada de la ecuación. Por favor, verifique la sintaxis.")
    sys.exit()  # Salir del programa

# Ingresar los extremos del intervalo (a y b)
try:
    a = float(input("Ingrese el extremo izquierdo del intervalo (a): "))
    b = float(input("Ingrese el extremo derecho del intervalo (b): "))
except ValueError:
    print("Error en la entrada. Asegúrese de ingresar números para los extremos del intervalo.")
    sys.exit()  # Salir del programa

# Elegir el umbral y el máximo de iteraciones
epsilon = 0.00001
max_iter = int(input("Ingrese el máximo de iteraciones: "))

# Llamar a la función del método de la bisección
root, iter_count = bisection_method(equation, a, b, epsilon, max_iter)

# Imprimir el resultado final
print(f"\nLa raíz es {root:.5f}, encontrada en {iter_count} iteraciones.")
