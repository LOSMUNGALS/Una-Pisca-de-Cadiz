print("Bienvenido a el restaurante Un Rincón de Cádiz,")
while True:
    reserva = str(input("¿Tienes reserva, si o no?: ")).lower()
    mesas_ya_reeservadas = [3,6,7,15,18]
    if reserva == "si":
        nombre = str(input("¿Cuál es el nombre con el que está registrada la reserva?: "))
        print(f"Bienvenido/a {nombre}, acompañeme a su mesa resevada.")
        break
    elif reserva == "no":
        while True:
            mesa = int(input("afortunadamente tenemos mesas disponibles, que mesa le gustaría, tenemos de la mesa 1 a la 20: "))
            if mesa in mesas_ya_reeservadas:
                print("Lo siento esa mesa ya esta ocupada o reservada, escoja otra por favor")
            elif mesa > 20 or mesa < 1:
                print("no tenemos ese numero de mesas, vuelva a intentar")
            else:
                print(f"Ok, dejame llevarte a tu mesa")
                break
        break
    else:
        print("por favor responde si o no")
print(f"Que tenga un buen día señor/a {nombre}")
