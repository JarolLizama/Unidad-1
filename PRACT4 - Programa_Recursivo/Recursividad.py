import time
import sys

# Configuración para permitir cálculos grandes en recursión
sys.setrecursionlimit(2000)

def fibonacci_iterativo(n):
    """Calcula Fibonacci de forma lineal usando un bucle."""
    if n <= 1: return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

def fibonacci_recursivo(n):
    """Calcula Fibonacci usando la definición matemática directa."""
    if n <= 1: return n
    return fibonacci_recursivo(n - 1) + fibonacci_recursivo(n - 2)

def comparar_rendimiento(n):
    print(f"--- Comparando Fibonacci para n = {n} ---")
    
    # Medir Iterativo
    inicio = time.perf_counter()
    res_i = fibonacci_iterativo(n)
    fin = time.perf_counter()
    tiempo_i = fin - inicio
    print(f"Iterativo: {res_i} | Tiempo: {tiempo_i:.8f} seg")

    # Medir Recursivo (Cuidado: n > 35 puede tardar mucho)
    if n <= 35:
        inicio = time.perf_counter()
        res_r = fibonacci_recursivo(n)
        fin = time.perf_counter()
        tiempo_r = fin - inicio
        print(f"Recursivo: {res_r} | Tiempo: {tiempo_r:.8f} seg")
        print(f"Diferencia: El iterativo es {tiempo_r/tiempo_i:.1f} veces más rápido")
    else:
        print("Recursivo: Saltado (n demasiado alto para recursión simple)")

if __name__ == "__main__":
    numero = int(input("Introduce el número de Fibonacci a calcular: "))
    comparar_rendimiento(numero)