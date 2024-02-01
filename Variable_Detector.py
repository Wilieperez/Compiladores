variable = "_Some$thingRandom"
state = "A"
position = 0
for i in variable:
    position = position + 1
    if state == "A":
        if i.isalpha() or i == "_":
            state = "B"
        else:
            state = "Z"
            print("No se esperaba '" + i + "' en la posicion", position)
            exit()
    elif state == "B":
        if i.isalpha() or i == "_" or i.isdigit():
            state = "B"
        else:
            state = "Z"
            print("No se esperaba '" + i + "' en la posicion", position)
            exit()

print("Variable correcta")