formula  = {
    "Area del triangulo": "(base * altura) / 2",
    "Area del rectangulo": "Area=base*altura",
    "Area del rombo": "area=diagonale mayor* diagonale menor/2",
    "Area del circulo": "(3.1416) * (radio * radio)",
    "Area del cuadrado": "lado * lado",
    "Area de un cono": "radio*generatriz",

}

try:
    print ("Formulas Matematicas")
    Formula2 = input("Ingresar Nombre de la Formula: ")
    print("La Formula para resolver {} es: {} ".format(Formula2, format(formula[Formula2],)))
except KeyError:
    print("La formula no existe") 