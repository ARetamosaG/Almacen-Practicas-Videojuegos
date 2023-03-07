class Room:
    """ This is a class """
    def __init__(self, description, north, south, east, west):
        """ This is the constructor """
        self.description = description
        self.north = north
        self.south = south
        self.east = east
        self.west = west


def main():
    room_list = []

    room = Room("Este es el torreón. Aquí dan clase los de bachillerato", 1, None, None, None)
    room_list.append(room)

    room = Room("Este es el departamento. Aquí descansan los profes", None, 0, None, 2)
    room_list.append(room)

    room = Room("Este es el claustro. Es el punto de encuentro del instituto", 5, None, 1, 3)
    room_list.append(room)

    room = Room("Este es el patio. Aquí juegan los niños", 4, None, 2, None)
    room_list.append(room)

    room = Room("Este es el laboratorio. Aquí van los de ciencias", None, 3, 5, None)
    room_list.append(room)

    room = Room("Este es el aula de musica. Mi favorita", None, 2, None, 4)
    room_list.append(room)

    current_room = 2

    done = False

    while not done:
        print()
        print(room_list[current_room].description)
        print()
        entrada = str(input("¿Que quieres hacer ahora?"))

        if entrada in ["N", "n", "North", "north", "NORTH"]:
            next_room = room_list[current_room].north

            if next_room is None:
                print("No hay salida")
            else:
                current_room = next_room

        elif entrada in ["S", "s", "South", "south", "SOUTH"]:
            next_room = room_list[current_room].south

            if next_room is None:
                print("No hay salida")
            else:
                current_room = next_room

        elif entrada in ["E", "e", "East", "east", "EAST"]:
            next_room = room_list[current_room].east

            if next_room is None:
                print("No hay salida")
            else:
                current_room = next_room

        elif entrada in ["W", "w", "West", "west", "WEST"]:
            next_room = room_list[current_room].west

            if next_room is None:
                print("No hay salida")
            else:
                current_room = next_room

        elif entrada in ["Q", "q", "Quit", "quit", "QUIT"]:

            quit_input = str(input("¿Seguro que quieres salir del juego?"))

            if quit_input in ["Y", "y", "yes", "YES", "Yes"]:
                print("Has abandonado el juego")
                done = True

            else:
                print("La entrada no es valida, sigues jugando")

        else:
            print("¡¡No he entendido tu entrada!! Prueba otra vez")


main()
