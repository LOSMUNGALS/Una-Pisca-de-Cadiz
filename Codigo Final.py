n1 = 1.18
n2 = 0.18

bebidas = {
    "agua": 50,
    "jugo de fresa": 100,
    "jugo de limon": 100,
    "jugo de chinola": 100,
    "agua con gas": 75,
    "coca cola": 90,
    "sprite": 90,
}

tapas = {
    "pinchos de camaron": 275,
    "camarones con garbanzo": 250,
    "tortillitas de camarones": 215,
    "pulpo a la gallega": 200,
    "patata brava": 310
}

menu = {
    "tortilla de papas": 250,
    "paella": 375,
    "gazpacho andaluz": 300,
    "cocido madrileño": 315,
    "paella valenciana": 395,
    "filete de merluza en papillote": 500,
    "bacalao al pil pil": 365
}

postres = {
    "tiramisu": 450,
    "churros con chocolate": 425,
    "brownies con helado": 300
}

descripcionbebidas = {
    "agua?": "buddy it's water -_-",
    "jugo de fresa?": "Jugo de fresa hechos de nuestras deliciosas fresas crecidas en nuestro campo.",
    "jugo de limon?": "Jugo de limon hechos de los limones más jugosos y dulces.",
    "jugo de chinola?": "Jugo de chinola hecho de las chinolas más frescas y maduras.",
    "agua con gas?": "agua + gas = agua con gas.",
    "coca cola?": "es un refresco dulce y con ligeero sabor a jarabe.",
    "sprite?": "refresco dulce con sabor a limón.",


descripcióntapas = {
    "pinchos de camaron?": "Brochetas com camarones y vegetales como pimentón y cebolla",
    "camarones con garbanzo?": "Asopado de garbanzos con vegetales y camarones, la salsa es de tomate",
    "tortillitas de camarones?": "Son tortillas que están hechas con harina de trigo y trozos de camarones, son crocantes",
    "pulpo a la gallega?": "Es una preparación de trosos de pulpo con papa sazonados con especias",
    "patata brava?": "Son papas con salsa de tomate arriba y sazonadas con orégano"
}

descripciónmenu = {
    "tortilla de papas?": "Una torilla hecha de harina de trigo, con papas y queso en el interior",
    "paella?": "Arroz sazonado con especias que tiene maricos y pescados",
    "gazpacho andaluz?": "Una sopa fría de tomate con vegetales en su interior",
    "cocido madrileño?": "Un asopado de mariscos con chicharrón y chorizo en su interior",
    "paella valenciana?": "Un arroz con maricos y pescados, pero con más vegetales que la paella normal",
    "filete de merluza en papillote?": "Un pedaso de un pescado llamado merluza que viene con vegetales alrededor",
    "bacalao al pil pil?": "Bacalao bañado en salsa de ajo, con tomates y champiñones alrededor"
}

descripciónpostres = {
    "tiramisu?": "Un tipo de pastel con café, crema, chocolate y vino evaporado",
    "churros con chocolate?": "Un set de chorros con chocolate aparte que pueden ser mojados en el",
    "brownies con helado?": "Un pedazo de brownie con un helado de vainilla por encima"
}
print("Bienvenido a el restaurante Un Rincón de Cádiz")
while True:
    reserva = str(input("¿Tienes reserva, si o no?: ")).lower()
    mesas_ya_reeservadas = [3,6,7,15,18]
    if reserva == "si":
        nombre = str(input("¿Cuál es el nombre con el que está registrada la reserva?: "))
        print(f"Bienvenido/a {nombre}, acompáñeme a su mesa reservada.")
        break
    elif reserva == "no":
        while True:
            mesa = int(input("Afortunadamente tenemos mesas disponibles, que mesa le gustaría, tenemos de la mesa 1 a la 20: "))
            if mesa in mesas_ya_reeservadas:
                print("Lo siento esa mesa ya esta ocupada o reservada, escoja otra por favor")
            elif mesa > 20 or mesa < 1:
                print("no tenemos ese numero de mesas, vuelva a intentar")
            else:
                print("Ok, dejame llevarte a tu mesa")
                break
        nombre = str(input("¿Cuál es su nombre?: "))
        print(f"Bienvenido/a {nombre}, acompáñeme a su mesa.")
        break
    else:
        print("Por favor responde si o no.")

print("Ahora, bienvenidos a Una Pisca de Cadiz, empezamos con las bebidas.")
total = 0

while True:
    print(bebidas)
    sabor = input("Elige una bebida (o escriba 'Nada mas' para terminar): ").lower()
    if sabor in bebidas:
        total += bebidas[sabor]
        print(f"Has elegido {sabor}. ¿Algo más?")
    elif sabor in descripcionbebidas:
        print(descripcionbebidas[sabor]
    elif sabor.lower() == "nada mas":
        break
    else:
        print("No tenemos esa bebida.")

while True:
    print(tapas)
    sabor = input("Elige una tapa (o escriba 'Nada mas' para terminar): ").lower()
    if sabor in tapas:
        total += tapas[sabor]
        print(f"Has elegido {sabor}. ¿Algo más?")
    elif sabor in descripcióntapas:
        print(descripcióntapas[sabor])
    elif sabor.lower() == "nada mas":
        break
    else:
        print("No tenemos ese plato.")

print("Seguimos con los platos principales.")

while True:
    print(menu)
    sabor = input("Elige un plato principal (o escriba 'Nada mas' para terminar): ").lower()
    if sabor in menu:
        total += menu[sabor]
        print(f"Has elegido {sabor}. ¿Algo más?")
    elif sabor in descripciónmenu:
        print(descripciónmenu[sabor])
    elif sabor.lower() == "nada mas":
        break
    else:
        print("No tenemos ese plato.")

print("Por último, terminamos con los postres.")

while True:
    print(postres)
    sabor = input("Elige un postre (o escriba 'Nada mas' para terminar): ").lower()
    if sabor in postres:
        total += postres[sabor]
        print(f"Has elegido {sabor}. ¿Algo más?")
    elif sabor in descripciónpostres:
        print(descripciónpostres[sabor])
    elif sabor.lower() == "nada mas":
        break
    else:
        print("No tenemos ese postre.")

impuestostotal = n2 * total
impuestos = total * n1
 
print(f"Su total es: {float(total)} pesos, con impuestos es {float(impuestos)}. También, el 18% de ITBIS en pesos es {float(impuestostotal)}")
tip = input("Si desea dar una propina, ingrese el monto de propina (si no quiere poner tip, ponga no)")
while True:
    if tip == "no":
        print(f"Okay, su total es: {float(total)} pesos, con impuestos es {float(impuestos)}. También, el 18% de ITBIS en pesos es {float(impuestostotal)}")
        break
    elif int(tip) > 0:
        totaltip = int(tip) + total
        totaltipimp = int(tip) + impuestos
        print(f"Okay, su nuevo total es: {float(totaltip)} pesos, con impuestos es {float(totaltipimp)}. Tambien, el 18% de ITBIS en pesos es {float(impuestostotal)}")
        break

while True:
    cardorcash = input("Vas a pagar con tarjeta o efectivo?: ").lower()
    if cardorcash == "tarjeta":
        balance = int(input("Ok, que balance tiene tu tarjeta?: "))
        if balance >= impuestos:
            print("La tarjeta paso perfectamente.")
            print(f"Que tenga buen dia y esperamos volverlo a ver, {nombre}.") 
            break
        elif balance < impuestos:
            print("Tu tarjeta no tiene suficiente balance")
            decision2 = input("Desearia pagar en efectivo?: ").lower()
        elif balance >= totaltipimp:
            print("La tarjeta paso perfectamente.")
            print(f"Que tenga buen dia y esperamos volverlo a ver, {nombre}.") 
            break
        elif balance < totaltipimp:
            print("La tarjeta no tiene suficiente balance.")
            decision2 = input("Desearia pagar en efectivo?: ").lower()
            break
    elif cardorcash == "efectivo":
        cantidadefectivo = int(input("Solo para saber cuanto sería el cambio, ¿con cuanto efectivo a va a pagar?, por favor no ponga la palabra pesos, solo la cantidad: "))
        cambio = cantidadefectivo-totaltipimp
        if cambio < 0:
            print(f"Lo siento, aun le faltan {float(cambio*-1)} por pagar")
        elif cambio == 0:
            print("Perfecto, no hay cambio")
            break
        elif cambio >= 0:
            print(f"Su cambio sería de {float(cambio)}")
            billetes = [2000, 1000, 500, 200, 100, 50, 25, 10, 5, 1]
            for i in billetes:
                cantidadbillete = cambio//i
                if cantidadbillete > 0:
                    print(f"{float(cantidadbillete)} x {i}")
                    cambio %= i
            break
    else:
        print("Solo tenemos tarjeta y efectivo")
