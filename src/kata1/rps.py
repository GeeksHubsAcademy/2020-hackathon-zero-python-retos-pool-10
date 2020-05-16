from random import randint

options = ["Piedra", "Papel", "Tijeras"]

# El resultado de salida son las siguientes String
#'Empate!'
#'Ganaste!'
#'Perdiste!'
def quienGana(player, ai):
    ply = player.capitalize()
    a = ai.capitalize()
    print(ply)
    print(a)
    if ply == a:
        return "Empate!"

    elif ply == options[2] and a == options[1]:
        return 'Ganaste!'

    elif ply == options[1] and a == options[0]:
        return 'Ganaste!'

    elif ply == options[0] and a == options[2]:
        return 'Ganaste!'
    
    else:
        return 'Perdiste'


# Entry Point
def Game():
    while True:
        try:
            print('Selecciona una de las siguientes opciones: ')
            print()
            print('Piedra: 1\nPapel: 2\nTijera: 3')
            print()
            player = int(input('Digita el número correspondiente a tu selección: \n')) - 1

            break
        except Exception as e:
            print(e)
            print('Opción invalida, intente nuevamente')
    
    ai = randint(0,2)
    print(f'Player selection: {options[player]}\n')
    print(f'ai selection: {options[ai]}\n')
    winner = quienGana(options[player], options[ai])

    print(winner)

# if __name__ == "__main__":
#     Game()

