
while True:
    totaltipimp = int(input("Hola: "))
    tipodepago = str(input("¿Que tipo de pago va a usar?, no tenemos transferencia, solo tarjeta y efectivo: ")).lower()
    if tipodepago == "tarjeta":
        print("espereme un momentico... Su tarjeta tiene balance suficiente... Listo, su almuerzo a sido pagado")
        break
    elif tipodepago == "efectivo":
        cantidadefectivo = int(input("Solo para saber cuanto sería el cambio, ¿con cuanto efectivo a va a pagar?, por favor no ponga la palabra pesos, solo la cantidad: "))
        cambio = cantidadefectivo-totaltipimp
        if cambio < 0:
            print(f"Lo siento, aun le faltan {cambio*-1} por pagar")
        elif cambio == 0:
            print("Perfecto, no hay cambio")
        elif cambio >= 0:
            print(f"Su cambio sería de {cambio}")
            billetes = [2000, 1000, 500, 200, 100, 50, 25, 10, 5, 1]
            for i in billetes:
                cantidadbillete = cambio//i
                if cantidadbillete > 0:
                    print(f"{cantidadbillete} x {i}")
                    cambio %= i
        break
    else:
        print("Solo tenemos tarjeta y efectivo")