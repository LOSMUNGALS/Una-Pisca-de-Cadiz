print("Bienvenido a el restaurante Un Rincón de Cádiz,")
while True:
    reserva = str(input("¿Tienes reserva, si o no?: ")).lower()
    mesas_ya_reeservadas = [3,6,7,15,18]
    if reserva == "si":
        nombre = str(input("¿Cuál es el nombre con el que está registrada la reserva?: "))
        print(f"Bienvenido/a {nombre}, acompañeme a su mesa resevada.")
    elif reserva == "no":
        while True:
            mesa = int(input("afortunadamente tenemos mesas disponibles, que mesa le gustaría, tenemos de la mesa 1 a la 20: "))
            if mesa in mesas_ya_reeservadas:
                print("Lo siento esa mesa ya esta ocupada o reservada, escoja otra por favor")
            elif mesa > 20 or mesa < 1:
                print("Invalid number, try again")
            else:
                print(f"Ok, let me take you to your table")
                break
        break
    else:
        print("please answer me with a yes or a no")
