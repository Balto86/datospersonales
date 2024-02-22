matriz = [[15, 10, 19],
          [31, 17, 11],
          [28, 41, 34]]
def bubble_sort_fila(fila):
    n = len(fila)
    for i in range(n -1):
        for j in range(n - i - 1):
            if fila[j] > fila[j + 1]:
                fila[j], fila[j + 1] = fila[j + 1], fila[j]

def mostrar_matriz(matriz):
    for fila in matriz:
        print(fila)
print("matriz original:")
mostrar_matriz(matriz)
for fila in matriz:
    bubble_sort_fila(fila)
print("\nMatriz ordenada por filas:")
mostrar_matriz(matriz)
