nombre = input("ingrese su nombre: ")
cantidad = int(input("ingresa la cantidad de la compra: "))
montoBruto = cantidad * 325
descuento = (montoBruto * 10) / 100
montoFinal = montoBruto - descuento
print(nombre, "usted compro", cantidad, "de", "cantidad")
print("monto sin descuento: dolares", montoBruto)
print("descuento: dolares", descuento)
print("usted debe pagar: dolares", montoFinal)
