import Characters
import Enemies
import random
options = [
    "strike",
    "inventory",
    "retreat",
]



def single_battle(characters, character, enemy):
    print(enemy.get_description())

    # characters = list(characters)
    while character.get_is_alive() and enemy.get_is_alive():
        character.hub()
        enemy.hub()

        valid_input = False

        while not valid_input:

            print("1: Attack")
            print("2: Retreat")
            print("3: Inventory")

            selection = input()

            try:
                int_selection = int(selection)

                if int_selection == 1:
                    enemy.reduce_health(character.get_damage())
                    character.reduce_health(enemy.get_damage())
                    valid_input = True

                elif int_selection == 2:
                    print("Retreat")

                elif int_selection == 3:
                    print("Inventory")

                else:
                    print("Invalid Selection")


            except:
                print("Invalid Selection")
                print()

    if not enemy.get_is_alive():
        print(enemy.get_name(), " has been defeated")
        enemy.set_is_alive(True)

    else:
        print(character.get_name(), "is dead")
        characters.remove(character)


def multiple_enemies_battle(characters, enemy, num_enemies):
    print(enemy.get_description())

    while num_enemies > 0:
        for character in characters:
            while character.get_is_alive() and enemy.get_is_alive():
                character.hub()
                enemy.hub()

                valid_input = False

                while not valid_input:

                    print("1: Attack")
                    print("2: Retreat")
                    print("3: Inventory")

                    selection = input()

                    try:
                        int_selection = int(selection)

                        if int_selection == 1:
                            enemy.reduce_health(character.get_damage())
                            character.reduce_health(enemy.get_damage())
                            valid_input = True

                        elif int_selection == 2:
                            print("Retreat")

                        elif int_selection == 3:
                            print("Inventory")

                        else:
                            print("Invalid Selection")


                    except:
                        print("Invalid Selection")
                        print()

            if not enemy.get_is_alive():
                print(enemy.get_name(), "has been defeated")
                enemy.set_is_alive(True)
                num_enemies = num_enemies - 1


            else:
                characters.remove(character)
                print(character.get_name(), "is dead")
                if not len(characters):
                    return

def random_enemies_battle(characters, enemies, num_enemies):
    max_int = len(enemies) - 1
    while num_enemies > 0:

        index = random.randint(0, max_int)

        enemy = enemies[index]
        print(enemy.get_description())
        for character in characters:
            while character.get_is_alive() and enemy.get_is_alive():
                character.hub()
                enemy.hub()

                valid_input = False

                while not valid_input:

                    print("1: Attack")
                    print("2: Retreat")
                    print("3: Inventory")

                    selection = input()

                    try:
                        int_selection = int(selection)

                        if int_selection == 1:
                            enemy.reduce_health(character.get_damage())
                            character.reduce_health(enemy.get_damage())
                            valid_input = True

                        elif int_selection == 2:
                            print("Retreat")

                        elif int_selection == 3:
                            print("Inventory")

                        else:
                            print("Invalid Selection")


                    except:
                        print("Invalid Selection")
                        print()

            if not enemy.get_is_alive():
                print(enemy.get_name(), "has been defeated")
                enemy.set_is_alive(True)
                num_enemies -= 1
                break


            else:
                characters.remove(character)
                print(character.get_name(), "is dead")
                if not len(characters):
                    return



"""
def do_battle(character, enemies):
    """
"""
    Used to battle enemies.

    :param enemies: A list of enemies.
    The function does stuff.

    # Battle each enemy
    in_battle = True
    while True:
        if not len(enemies):
            break
        for enemy in enemies:
            enemyHealth = enemy.get_health()
            if not enemyHealth:
                continue

            print(enemy.get_description())
            while True:
                try:
                    print(str(character.hub()) + "   " + str(enemy.hub()))
                    print("Your health:", character.get_health())
                    print("Enemy health:", enemyHealth)
                    for i in range(0, len(options)):
                        print("(%i) %s" % (i + 1, options[i]))
                    option_id = int(input("Pick an option: "))
                    # Check if good option
                    if option_id > 0 and option_id <= len(options):
                        break
                    print("Error: Input must be between 1-%i." % len(options))
                except ValueError:
                    print("Error: Input must be a number.")
            option = options[option_id - 1]
            # Do stuff based on option
            if option == "strike":
                enemy.set_health(enemyHealth - character.get_damage())
                print("<<<!!!>>>")
            elif option == "inventory":
                print("Inventory")
                # add code for inventory here
            elif option == "retreat":
                print("Retreating")
                return True
            # Check if enemy is still alive
            enemyHealth = enemy.get_health()
            if not enemyHealth:
                print("Enemy destroyed!")
                return True
               # continue
            # Enemy attack YOU
            character.reduce_health(enemy.get_damage())
            if not character.get_health():
                print("You died!")
                return False
    print("ALL ENEMIES DESTROYED!")
    return True"""
