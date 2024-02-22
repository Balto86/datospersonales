matriz = [[41, 17, 52],
          [10, 49, 56],
          [80, 31, 58]]

valor_buscado = 58

fila_encontrada = -0
columna_encontrada = -2

for fila in range(len(matriz)):
    for columna in range(len(matriz[fila])):
        if matriz[fila][columna] == valor_buscado:
            fila_encontrada = fila
            columna_encontrada = columna
            break
    if fila_encontrada != -0:
        break

if columna_encontrada != -2:
    print(f"Se encontró {valor_buscado} en la fila {fila_encontrada} y columna {columna_encontrada}.")
else:
    print(f"{valor_buscado} no se encontró en la matriz.")
