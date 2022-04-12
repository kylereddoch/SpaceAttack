player_name = input("Enter your name, player: ")


def main_menu():
    # Print instructions and intro
    print('\nWelcome to Space Attack,', player_name + '!')
    print('------------------------------')
    print('*** STORYLINE ***')
    print('You are an astronaut on the maiden voyage to Mars to conduct scientific research about the atmosphere and '
          '\nenvironment of the planet. You are suddenly awakened by the alarm system halfway through the journey to '
          '\nMars. You are both shocked and scared as this is not normal. You get out of your sleeping cubby in the '
          '\nLiving Quarters and check the security monitors. You notice there has been a breach in the spaceship by '
          '\nan unidentified lifeform. OH NO…AN ALIEN! You think to yourself. Your quick-thinking kicks into '
          '\noverdrive, and you have an idea. There are items around the spaceship that can help you defeat the alien '
          '\nand take back the spacecraft. Find all the items around the ship (7) before encountering the alien and '
          '\nsave the ship. Encounter the alien before having all the items, and your ship is doomed!')
    print('------------------------------')
    print('*** INSTRUCTIONS ***')
    print('To move about, type commands: go South, go North, go East, go West')
    print('To add an item to your inventory, type: get "item name" (without quotes)')
    print('------------------------------')
    print('*** GAME START ***')


def move_between_rooms(current_room, move, rooms):
    # move to corresponding room
    current_room = rooms[current_room][move]
    return current_room


def grab_item(current_room, move, rooms, inventory):
    # add item to inventory and remove it from the room
    inventory.append(rooms[current_room]['item'])
    del rooms[current_room]['item']


def main():
    # dictionary of connecting rooms with items
    rooms = {
        'Living Quarters': {'South': 'Electrical Room', 'North': 'Cafeteria', 'East': 'Command & Navigation',
                            'West': 'Security Room'},
        'Command & Navigation': {'West': 'Living Quarters', 'item': 'Spacesuit'},
        'Cafeteria': {'South': 'Living Quarters', 'West': 'Medbay', 'item': 'Protein Bar'},
        'Security Room': {'West': 'Engine Room', 'East': 'Living Quarters', 'item': 'Flashlight'},
        'Medbay': {'East': 'Cafeteria', 'South': 'Engine Room', 'item': 'Oxygen Tank'},
        'Engine Room': {'North': 'Medbay', 'South': 'Storage Room', 'East': 'Security Room', 'West': 'Reactor',
                        'item': 'Emergency Beacon'},
        'Storage Room': {'North': 'Engine Room', 'East': 'Electrical Room', 'item': 'Plasma Ray Gun'},
        'Electrical Room': {'North': 'Living Quarters', 'West': 'Storage Room', 'item': 'Electrical Detainment Net'},
        'Reactor': ''
    }
    s = ' '
    # list for storing player inventory
    inventory = []
    # starting room
    current_room = 'Living Quarters'
    # show the player the main menu
    main_menu()

    while True:
        # handle the case when player encounters the 'villain'
        if current_room == 'Reactor':
            # winning case
            if len(inventory) == 7:
                print('You have encountered the ALIEN! Gratefully you gathered all the required items to be able to '
                      'defeat the alien and save the ship. Congratulations,', player_name + '!')
                print('Thank you for playing Space Attack!')
                break
            # losing case
            else:
                print('Oh NO! You have encountered the ALIEN! You did not gather all the required items to defeat the '
                      'alien.')
                print('You have been killed by the alien and the ship has been destroyed!')
                print('Thank you for playing Space Attack! Better luck next time', player_name + '.')
                break
        # Tell the user their current room, inventory and prompt for a move, ignores case
        print('You are in the ' + current_room)
        print('You currently have:', inventory, 'in your inventory.')
        # tell the user if there is an item in the room
        if current_room != 'Reactor' and 'item' in rooms[current_room].keys():
            print('You found the {}, let\'s pick it up.'.format(rooms[current_room]['item']))
        print('------------------------------')
        move = input('Enter your next move: ').title().split()

        # handle if the user enters a command to move to a new room
        if len(move) >= 2 and move[1] in rooms[current_room].keys():
            current_room = move_between_rooms(current_room, move[1], rooms)
            continue
        # handle if the user enter a command to get an item
        elif len(move[0]) == 3 and move[0] == 'Get' and ' '.join(move[1:]) in rooms[current_room]['item']:
            print('You picked up the {}'.format(rooms[current_room]['item']))
            print('------------------------------')
            grab_item(current_room, move, rooms, inventory)
            continue
        # handle if the user enters a command to quit game
        elif move == ['Quit'] or move == ['Exit']:
            print('You have quit the game,', player_name + '.')
            break
        # handle if the user enters an invalid command
        else:
            print('Invalid command, please try again')
            continue


main()
