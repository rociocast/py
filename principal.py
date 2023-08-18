
count_humano =0
count_computador =0

print("Piedra, Papel o Tijeras\n")
print("Bienvenid@, comencemos...\n")
keep_playing = True
while keep_playing:
    import random


    print("Selecciona una opción: ")
    #print("Piedra,")
    #print("Papel")
    #print("Tijeras")
    hum_choice = input(['Piedra', 'Papel', 'Tijeras'])
    print('Has escogido: ' + hum_choice)

    comp_choice = random.choice(['Piedra', 'Papel', 'Tijeras'])
    print('\nLa computadora escoge: ' + comp_choice)

    if((hum_choice=='Piedra' and comp_choice=='Tijeras') or (hum_choice=='Tijeras' and comp_choice=='Papel') or(hum_choice=='Papel' and comp_choice=='Piedra')):
        print("Ganaste")
        count_humano += 1
    elif(hum_choice == comp_choice):
        print("Empate")
    else :
        print("Ganó la computadora")
        count_computador += 1

    print("\n¿Quieres volver a jugar?")
    answer = input()
    if answer == "No":
        keep_playing = False
        print("\nGracias por jugar!")
        print("El puntaje de la computadora es: "+str(count_computador))
        print("Tu puntaje es: " + str(count_humano))

        print("\nResultados Finales:")
        if count_computador > count_humano:
            print("Mejor suerte para la próxima!\n")
        elif count_computador == count_humano:
            print("Esto es un empate\n")
        else :
            print("GANASTE!\n")
        print("***Piedra, Papel o Tijeras***")